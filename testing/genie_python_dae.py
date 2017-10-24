"""
A manual system test for exercising genie_python dae functionality
"""
def genie_python_dae_test():
    
    def float_in_tolerance(actual, expected, tolerance=0.0005):
        return abs(actual-expected)<tolerance
        
    def assert_from_user_input(question):  
        assert (raw_input("{}? (Y/N) ".format(question)).lower()+"n")[0]=="y"
        
    print "Test get/set title"
    new_title = "NEW TITLE"
    g.change_title(new_title)
    assert g.get_title()==new_title
    
    print "Test get/set users"
    new_users = "Adrian, Kevin, Kathryn"
    g.change_users(new_users)
    # DAE replaces final "," with "and"
    assert g.get_dashboard()['user'].replace(" and", ",")==new_users
    
    print "Test change run state"
    # Use a range of verbosities
    assert g.get_runstate()=="SETUP"
    g.begin(True)
    assert g.get_runstate()=="RUNNING"
    g.pause()
    assert g.get_runstate()=="PAUSED"
    g.resume(False)
    assert g.get_runstate()=="RUNNING"
    g.abort(None)
    assert g.get_runstate()=="SETUP"
    g.begin(True)
    assert g.get_runstate()=="RUNNING"
    g.end(False)
    assert g.get_runstate()=="SETUP"

    print "Testing waitfors"    
    g.waitfor_time(seconds=0.1)
    g.waitfor_uamps(0.1)
    g.waitfor_frames(1)
    
    print "TESTS COMPLETED SUCCESSFULLY"
    