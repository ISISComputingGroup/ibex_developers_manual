from genie_python import genie as g

"""
A manual system test for exercising genie_python block functionality
"""
def genie_python_blocks_test():

    str_block_name = "TEST_BLOCK_STR"
    num_block_name = "TEST_BLOCK_NUM"
    
    def float_in_tolerance(actual, expected, tolerance=0.0005):
        return abs(actual-expected)<tolerance
        
    def assert_numeric_block(name, value=None, runcontrol=None, lowlimit=None, highlimit=None, connected=None, max_wait=10):

        import time

        steps = 10
        for i in range(steps):
            try:
                block = g.cget(num_block_name)
                if value is not None:
                    assert float_in_tolerance(block['value'], value)
                if lowlimit is not None:
                    assert float_in_tolerance(block['lowlimit'], lowlimit)
                if highlimit is not None:
                    assert float_in_tolerance(block['highlimit'], highlimit)
                if connected is not None:
                    assert block['connected']==connected
                if runcontrol is not None:
                    assert block['runcontrol']==runcontrol
                return
            except AssertionError:
                if i < steps-1:
                    time.sleep(float(max_wait)/float(steps))
                else:
                    print("Expected value: {}, {}, {}, {}, {}. Actual value: {}, {}, {}, {}, {} (val, connected, rc, low, high)".format(
                        value, connected, runcontrol, lowlimit, highlimit,
                        block['value'], block['connected'], block['runcontrol'], block['lowlimit'], block['highlimit']))
                    assert False
                    
    def assert_from_user_input(question):  
        assert (input("{}? (Y/N) ".format(question)).lower()+"n")[0]=="y"
        

    print("Test required blocks exist")
    assert num_block_name in g.get_blocks()
    assert str_block_name in g.get_blocks()
    
    print("Test can set block values")
    new_str_value = "TEST"
    g.cset(str_block_name, new_str_value)
    assert g.cget(str_block_name)['value']==new_str_value
    
    new_num_value = 1.234
    g.cset(num_block_name, new_num_value)
    assert_numeric_block(num_block_name, value=new_num_value)
    
    print("Test setting run control")
    starting_value = 0.0
    lowlimit = -1.0
    highlimit = 1.0
    g.cset(num_block_name, starting_value, runcontrol=True, lowlimit=lowlimit, highlimit=highlimit)
    assert_numeric_block(num_block_name, lowlimit=lowlimit, highlimit=highlimit, runcontrol=True, value=starting_value)
    assert_from_user_input("Is TEST_BLOCK_NUM displaying within its run control limit")
    
    g.cset(num_block_name, highlimit+1.0)
    assert_from_user_input("Is TEST_BLOCK_NUM displaying outside its run control limit")
    g.cset(num_block_name, starting_value)
    
    print("Test show block data")
    g.cshow(num_block_name)
    assert_from_user_input("Does the data above look sensible for TEST_BLOCK_NUM")
    g.cshow(str_block_name)
    assert_from_user_input("Does the data above look sensible for TEST_BLOCK_STR")
    
    print("TESTS COMPLETED SUCCESSFULLY")
    