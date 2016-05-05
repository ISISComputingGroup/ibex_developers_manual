<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  
  


  <head>
    <title>
      EPICS_basics.rst in trunk/isisdoc/misc_docs
     – ISIS EPICS
    </title>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
      <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <!--[if IE]><script type="text/javascript">
      if (/^#__msie303:/.test(window.location.hash))
        window.location.replace(window.location.hash.replace(/^#__msie303:/, '#'));
    </script><![endif]-->
        <link rel="search" href="/EPICS/search" />
        <link rel="help" href="/EPICS/wiki/TracGuide" />
        <link rel="alternate" href="/EPICS/browser/trunk/isisdoc/misc_docs/EPICS_basics.rst?format=txt" type="text/plain" title="Plain text" /><link rel="alternate" href="/EPICS/export/3115/trunk/isisdoc/misc_docs/EPICS_basics.rst" type="text/prs.fallenstein.rst; charset=iso-8859-15" title="Original format" />
        <link rel="start" href="/EPICS/wiki" />
        <link rel="stylesheet" href="/EPICS/chrome/common/css/trac.css" type="text/css" /><link rel="stylesheet" href="/EPICS/chrome/common/css/code.css" type="text/css" /><link rel="stylesheet" href="/EPICS/chrome/common/css/browser.css" type="text/css" />
        <link rel="prev" href="/EPICS/browser/trunk/isisdoc/misc_docs/EPICS_basics.rst?rev=1785" title="Revision 1785" />
        <link rel="shortcut icon" href="/EPICS/chrome/common/trac.ico" type="image/x-icon" />
        <link rel="icon" href="/EPICS/chrome/common/trac.ico" type="image/x-icon" />
    <style id="trac-noscript" type="text/css">.trac-noscript { display: none !important }</style>
      <link type="application/opensearchdescription+xml" rel="search" href="/EPICS/search/opensearch" title="Search ISIS EPICS" />
      <script type="text/javascript" charset="utf-8" src="/EPICS/chrome/common/js/jquery.js"></script>
      <script type="text/javascript" charset="utf-8" src="/EPICS/chrome/common/js/babel.js"></script>
      <script type="text/javascript" charset="utf-8" src="/EPICS/chrome/common/js/messages/en_GB.js"></script>
      <script type="text/javascript" charset="utf-8" src="/EPICS/chrome/common/js/trac.js"></script>
      <script type="text/javascript" charset="utf-8" src="/EPICS/chrome/common/js/search.js"></script>
    <script type="text/javascript">
      jQuery("#trac-noscript").remove();
      jQuery(document).ready(function($) {
        $(".trac-autofocus").focus();
        $(".trac-target-new").attr("target", "_blank");
        setTimeout(function() { $(".trac-scroll").scrollToTop() }, 1);
        $(".trac-disable-on-submit").disableOnSubmit();
      });
    </script>
    <script type="text/javascript" src="/EPICS/chrome/common/js/folding.js"></script>
    <script type="text/javascript">
      jQuery(document).ready(function($) {
        $(".trac-toggledeleted").show().click(function() {
                  $(this).siblings().find(".trac-deleted").toggle();
                  return false;
        }).click();
        $("#jumploc input").hide();
        $("#jumploc select").change(function () {
          this.parentNode.parentNode.submit();
        });
          $('#preview table.code').enableCollapsibleColumns($('#preview table.code thead th.content'));
      });
    </script>
  </head>
  <body>
    <div id="banner">
      <div id="header">
        <a id="logo" href="/EPICS/wiki/TracIni#header_logo-section"><img src="/EPICS/chrome/site/your_project_logo.png" alt="(please configure the [header_logo] section in trac.ini)" /></a>
      </div>
      <form id="search" action="/EPICS/search" method="get">
        <div>
          <label for="proj-search">Search:</label>
          <input type="text" id="proj-search" name="q" size="18" value="" />
          <input type="submit" value="Search" />
        </div>
      </form>
      <div id="metanav" class="nav">
    <ul>
      <li class="first"><a href="/EPICS/login">Login</a></li><li><a href="/EPICS/prefs">Preferences</a></li><li><a href="/EPICS/wiki/TracGuide">Help/Guide</a></li><li class="last"><a href="/EPICS/about">About Trac</a></li>
    </ul>
  </div>
    </div>
    <div id="mainnav" class="nav">
    <ul>
      <li class="first"><a href="/EPICS/wiki">Wiki</a></li><li><a href="/EPICS/timeline">Timeline</a></li><li><a href="/EPICS/roadmap">Roadmap</a></li><li class="active"><a href="/EPICS/browser">Browse source</a></li><li><a href="/EPICS/report">View tickets</a></li><li class="last"><a href="/EPICS/search">Search</a></li>
    </ul>
  </div>
    <div id="main">
      <div id="ctxtnav" class="nav">
        <h2>Context navigation</h2>
        <ul>
          <li class="first"><span>&larr; <a class="prev" href="/EPICS/browser/trunk/isisdoc/misc_docs/EPICS_basics.rst?rev=1785" title="Revision 1785">Previous revision</a></span></li><li><span class="missing">Next revision &rarr;</span></li><li><a href="/EPICS/browser/trunk/isisdoc/misc_docs/EPICS_basics.rst?annotate=blame" title="Annotate each line with the last changed revision (this can be time consuming...)">Blame</a></li><li class="last"><a href="/EPICS/log/trunk/isisdoc/misc_docs/EPICS_basics.rst">Revision log</a></li>
        </ul>
        <hr />
      </div>
    <div id="content" class="browser">
        <h1>
          
<a class="pathentry first" href="/EPICS/browser?order=name" title="Go to repository root">source:</a>
<a class="pathentry" href="/EPICS/browser/trunk?order=name" title="View trunk">trunk</a><span class="pathentry sep">/</span><a class="pathentry" href="/EPICS/browser/trunk/isisdoc?order=name" title="View isisdoc">isisdoc</a><span class="pathentry sep">/</span><a class="pathentry" href="/EPICS/browser/trunk/isisdoc/misc_docs?order=name" title="View misc_docs">misc_docs</a><span class="pathentry sep">/</span><a class="pathentry" href="/EPICS/browser/trunk/isisdoc/misc_docs/EPICS_basics.rst?order=name" title="View EPICS_basics.rst">EPICS_basics.rst</a>
<br style="clear: both" />

        </h1>
        <div id="diffrev">
          <form action="/EPICS/changeset" method="get">
            <div>
              <label title="Show the diff against a specific revision">
                View diff against: <input type="text" name="old" size="6" />
                <input type="hidden" name="old_path" value="trunk/isisdoc/misc_docs/EPICS_basics.rst" />
                <input type="hidden" name="new" />
                <input type="hidden" name="new_path" value="trunk/isisdoc/misc_docs/EPICS_basics.rst" />
              </label>
            </div>
          </form>
        </div>
        <div id="jumprev">
          <form action="" method="get">
            <div>
              <label for="rev">
                View revision:</label>
              <input type="text" id="rev" name="rev" size="6" />
            </div>
          </form>
        </div>
        <div id="jumploc">
          <form action="" method="get">
            <div class="buttons">
              <label for="preselected">Visit:</label>
              <select id="preselected" name="preselected">
                <option selected="selected"></option>
                <optgroup label="branches">
                  <option value="/EPICS/browser/trunk">trunk</option><option value="/EPICS/browser/branches/ORIG">branches/ORIG</option>
                </optgroup><optgroup label="tags">
                  <option value="/EPICS/browser/tags/lvDCOM-1_0?rev=511">tags/lvDCOM-1_0</option>
                </optgroup>
              </select>
              <input type="submit" value="Go!" title="Jump to the chosen preselected path" />
            </div>
          </form>
        </div>
        <div class="trac-tags">
        </div>
      <table id="info" summary="Revision info">
        <tr>
          <th>
                <a href="/EPICS/changeset/2305/trunk/isisdoc/misc_docs/EPICS_basics.rst" title="View differences">Last change</a>
                  on this file was
                  <a href="/EPICS/changeset/2305/" title="View changeset 2305">2305</a>,
                  checked in by faa59, <a class="timeline" href="/EPICS/timeline?from=2014-12-03T10%3A59%3A06Z&amp;precision=second" title="See timeline at 3 Dec 2014 10:59:06">17 months ago</a>
          </th>
        </tr>
        <tr>
          <td class="message searchable">
              <p>
Fix image links<br />
</p>
          </td>
        </tr>
        <tr><td colspan="2">
            <strong>File size:</strong>
            <span title="28463 bytes">27.8 KB</span>
          </td></tr>
      </table>
      <div id="preview" class="searchable">
        
  <div class="document" id="epics-basics">
<h1 class="title">EPICS Basics</h1>
<div class="section" id="building-epics-with-vs2012-express-on-a-64bit-windows">
<h1>Building EPICS with VS2012 Express on a 64bit Windows</h1>
<ol class="arabic">
<li><p class="first">Download and install Visual Studio Express 2012 for Windows Desktop</p>
</li>
<li><p class="first">Download and install Strawberry Perl (64 bit version) to <tt class="docutils literal"><span class="pre">C:\strawberry\</span></tt></p>
</li>
<li><p class="first">Download, unzip and copy GNU Make for Windows to <tt class="docutils literal"><span class="pre">C:\gnuwin32</span></tt></p>
</li>
<li><p class="first">Download LibIntl for Windows, LibIconv for Windows as they contain dlls we need for gnumake.</p>
</li>
<li><p class="first">Extract the files and copy <tt class="docutils literal">libintl3.dll</tt>, <tt class="docutils literal">libiconv2.dll</tt> and copy to <tt class="docutils literal"><span class="pre">C:\gnuwin32\bin\</span></tt> (i.e. the same directory as make)</p>
</li>
<li><p class="first">Create a directory such as <tt class="docutils literal"><span class="pre">C:\EPICS</span></tt>. Download and unzip EPICS base (3.14.12.3). Move and rename base to <tt class="docutils literal"><span class="pre">C:\EPICS\base</span></tt>. <strong>Note:</strong> you may need to install 7-Zip to unzip EPICS base</p>
</li>
<li><dl class="first docutils">
<dt>Open <tt class="docutils literal"><span class="pre">C:\EPICS\base\startup\win32.bat</span></tt> and check/change the following settings:</dt>
<dd><ul class="first last simple">
<li>check the perl path is correct; for example it might be set <tt class="docutils literal"><span class="pre">PATH=C:\strawberry\perl\bin;%PATH%</span></tt></li>
<li>check the gnuwin32 path is correct</li>
<li>comment out the <tt class="docutils literal">call <span class="pre">C:\Program</span> files\Microsoft Visual Studio 10.0\VC\vcvarsall.bat&quot; x86</tt> line</li>
<li>below that add the following line: call <tt class="docutils literal"><span class="pre">C:\Program</span> Files <span class="pre">(x86)\Microsoft</span> Visual Studio 11.0\VC\vcvarsall.bat&quot; x86_amd64</tt>. <strong>NOTE:</strong> we are using the cross-compiler to build 64bit EPICS, hence &quot;x86_amd64&quot; rather than &quot;x64&quot;.</li>
<li>uncomment the <tt class="docutils literal">set <span class="pre">EPICS_HOST_ARCH=windows-x64</span></tt> line and comment out the <tt class="docutils literal">set <span class="pre">EPICS_HOST_ARCH=win32-x86</span></tt></li>
<li>comment out the <tt class="docutils literal">set <span class="pre">PATH=%PATH%;C:\Program</span> files\Bazaar</tt> line</li>
<li>Save the file.</li>
</ul>
</dd>
</dl>
</li>
<li><dl class="first docutils">
<dt>Open a standard command line prompt and type the following:</dt>
<dd><ul class="first last simple">
<li><tt class="docutils literal">cd <span class="pre">C:\EPICS\base\startup</span></tt></li>
<li><tt class="docutils literal">win32.bat</tt></li>
<li><tt class="docutils literal">cd ..</tt></li>
<li><tt class="docutils literal">make</tt></li>
</ul>
</dd>
</dl>
</li>
</ol>
<p>It should build now, taking about 5-10 minutes.</p>
<div class="section" id="preparing-to-use-epics">
<h2>Preparing to use EPICS</h2>
<ol class="arabic">
<li><dl class="first docutils">
<dt>Add some environment variables:</dt>
<dd><ul class="first last simple">
<li><tt class="docutils literal"><span class="pre">EPICS_HOST_ARCH=windows-x64</span></tt></li>
<li><tt class="docutils literal"><span class="pre">EPICS=C:\EPICS\</span></tt></li>
</ul>
</dd>
</dl>
</li>
<li><p class="first">Add the following directory to the PATH environment variable:</p>
<pre class="literal-block">
%EPICS%\base\bin\%EPICS_HOST_ARCH%
</pre>
</li>
</ol>
</div>
<div class="section" id="to-build-a-debug-version">
<h2>To build a debug version</h2>
<ol class="arabic">
<li><dl class="first docutils">
<dt>Edit <tt class="docutils literal">startup\win32.bat</tt></dt>
<dd><ul class="first last simple">
<li>Change <tt class="docutils literal">set <span class="pre">EPICS_HOST_ARCH=windows-x64</span></tt> line to <tt class="docutils literal">set <span class="pre">EPICS_HOST_ARCH=windows-x64-debug</span></tt></li>
</ul>
</dd>
</dl>
</li>
</ol>
<p>Then rebuild using make.</p>
</div>
</div>
<div class="section" id="creating-a-simple-ioc">
<h1>Creating a simple IOC</h1>
<p>Run Win32.bat from <tt class="docutils literal">$EPICS_BASE\startup</tt></p>
<p>Create a directory in the directory below EPICS base called <tt class="docutils literal">my_iocs</tt> or whatever.
Inside that create a directory called <tt class="docutils literal">simpleioc</tt>.</p>
<p>From inside <tt class="docutils literal">simpleioc</tt>, type the following:</p>
<pre class="literal-block">
makeBaseApp.pl -t ioc simple
makeBaseApp.pl -i -t ioc simple
</pre>
<p>Accept the default name (i.e. press Return)</p>
<p>Move to the Db directory:</p>
<pre class="literal-block">
cd simpleApp\Db
</pre>
<p>Create a file called simple.db:</p>
<pre class="literal-block">
echo. 2&gt;simple.db
</pre>
<p>Open it in notepad (or similar) and add the following records and save the file:</p>
<pre class="literal-block">
record(ai, &quot;simple:value1&quot;)
{
    field(VAL, 1)
}
record(ai, &quot;simple:value2&quot;)
{
    field(VAL, 2)
}
record(calc,&quot;simple:diff&quot;)
{
    field(SCAN,&quot;1 second&quot;)
    field(INPA, &quot;simple:value1&quot;)
    field(INPB, &quot;simple:value2&quot;)
    field(&quot;CALC&quot;, &quot;A - B&quot;)
}
</pre>
<p>Open the Makefile in the Db directory and add the following near where it says <tt class="docutils literal">#DB += xxx.db</tt>:</p>
<pre class="literal-block">
DB += simple.db
</pre>
<p>Save it!</p>
<p>Move back up to the simpleioc directory and type <tt class="docutils literal">make</tt>. After it completes successfully move to the <tt class="docutils literal">iocBoot\iocsimple</tt> directory
Edit the st.cmd file:</p>
<pre class="literal-block">
Change #dbLoadRecords(&quot;db/xxx.db&quot;,&quot;user=blahblah&quot;) to dbLoadRecords(&quot;db/simple.db&quot;,&quot;user=blahblah&quot;)
</pre>
<p>Save it!</p>
<p>Now to start the IOC by typing the following from the iocBootiocsimpledirectory:</p>
<pre class="literal-block">
..\..\bin\windows-x64\simple.exe st.cmd
</pre>
<p>The IOC should start.
Type dbl to print a list of PVs. If the PVs are not there then read the the IOC start up messages to see
if there is an error.</p>
<p>If you start a new command line and set the paths as above if it will be possible to use <tt class="docutils literal">caput</tt>, <tt class="docutils literal">caget</tt> etc.
If you edit the records, you may need to run make again - just stop the IOC, type make and then restart the IOC.</p>
</div>
<div class="section" id="creating-a-random-number-generator-ioc">
<h1>Creating a random number generator IOC</h1>
<p>Largely based on the tutorial found <a class="reference external" href="https://pubweb.bnl.gov/~mdavidsaver/epics-doc/epics-devsup.html">here</a>.</p>
<p>Run Win32.bat from <tt class="docutils literal">$EPICS_BASE\startup</tt></p>
<p>Create a directory called <tt class="docutils literal">random</tt> and move to it. Run the following commands (accept the defaults):</p>
<pre class="literal-block">
makeBaseApp.pl -t ioc rand
makeBaseApp.pl -i -t ioc rand
</pre>
<p>Move to the <tt class="docutils literal">randApp\src directory</tt>. Create the dbd file:</p>
<pre class="literal-block">
echo. 2&gt;randdev.dbd
</pre>
<p>Open and add the following:</p>
<pre class="literal-block">
device(ai,CONSTANT,devAiRand,&quot;Random&quot;)
</pre>
<p>Create the C file:</p>
<pre class="literal-block">
echo. 2&gt;devrand.c
</pre>
<p>Open and add the following:</p>
<pre class="literal-block">
#include &lt;stdlib.h&gt;
#include &lt;epicsExport.h&gt;
#include &lt;dbAccess.h&gt;
#include &lt;devSup.h&gt;
#include &lt;recGbl.h&gt;
#include &lt;aiRecord.h&gt;
static long init_record(aiRecord *pao);
static long read_ai(aiRecord *pao);
struct randState {
  unsigned int seed;
};
struct {
  long num;
  DEVSUPFUN  report;
  DEVSUPFUN  init;
  DEVSUPFUN  init_record;
  DEVSUPFUN  get_ioint_info;
  DEVSUPFUN  read_ai;
  DEVSUPFUN  special_linconv;
} devAiRand = {
  6, /* space for 6 functions */
  NULL,
  NULL,
  init_record,
  NULL,
  read_ai,
  NULL
};
epicsExportAddress(dset,devAiRand);
static long init_record(aiRecord *pao)
{
  struct randState* priv;
  unsigned long start;
  priv=malloc(sizeof(struct randState));
  if(!priv){
    recGblRecordError(S_db_noMemory, (void*)pao, &quot;devAoTimebase failed to allocate private struct&quot;);
    return S_db_noMemory;
  }
  recGblInitConstantLink(&amp;pao-&gt;inp,DBF_ULONG,&amp;start);
  priv-&gt;seed=start;
  pao-&gt;dpvt=priv;
  srand(&amp;priv-&gt;seed);
  return 0;
}
static long read_ai(aiRecord *pao)
{
  struct randState* priv=pao-&gt;dpvt;
  pao-&gt;rval=rand() % 100;
  return 0;
}
</pre>
<p>Edit <tt class="docutils literal">randApp\src\MakeFile</tt> and add the following in the appropriate places:</p>
<pre class="literal-block">
rand_DBD += randdev.dbd
rand_SRCS += devRand.c
</pre>
<p>Move to the <tt class="docutils literal">randApp\Db directory</tt>. Create the db file:</p>
<pre class="literal-block">
echo. 2&gt;rand.db
</pre>
<p>Open and edit it to read:</p>
<pre class="literal-block">
record(ai,&quot;test:rand&quot;){
    field(DTYP,&quot;Random&quot;)
    field(DESC,&quot;Random numbers&quot;)
    field(SCAN,&quot;1 second&quot;)
    field(INP,&quot;$(S)&quot;)
}
</pre>
<p>Edit <tt class="docutils literal">randApp\Db\Makefile</tt> and add:</p>
<blockquote>
DB += rand.db</blockquote>
<p>Move to <tt class="docutils literal">&lt;top&gt;</tt> and run <tt class="docutils literal">make</tt></p>
<p>Move to <tt class="docutils literal">iocBoot\iocrand\</tt></p>
<p>Edit the appropriate parts of st.cmd to look like this:</p>
<pre class="literal-block">
## Register all support components
dbLoadDatabase &quot;dbd/rand.dbd&quot;
rand_registerRecordDeviceDriver pdbbase
## Load record instances
dbLoadRecords(&quot;db/rand.db&quot;, S=324235&quot;)
</pre>
<p>Now run the IOC:</p>
<pre class="literal-block">
..\..\bin\windows-x64\rand.exe st.cmd
</pre>
</div>
<div class="section" id="procserver">
<h1>ProcServer</h1>
<div class="section" id="installation">
<h2>Installation</h2>
<p>Download the Windows executable from <a class="reference external" href="http://sourceforge.net/projects/procserv/">http://sourceforge.net/projects/procserv/</a> and install somewhere in your EPICS installation. For example: <tt class="docutils literal"><span class="pre">C:\EPICS_PILOT\support\procserver</span></tt>.
Obtain <tt class="docutils literal">CygWin1.dll</tt> and put it into the ProcServer directory (installing CygWin and copying and pasting the file is one way).</p>
<p>Add the ProcServer directory to your EPICS path; for example: edit the .bat file that is used to configure your EPICS environment.</p>
</div>
<div class="section" id="running-a-simple-example">
<h2>Running a simple example</h2>
<p>From the command line, move to the iocBoot directory of an IOC (e.g. <tt class="docutils literal"><span class="pre">C:\EPICS_PILOT\ISIS\simpleioc\iocBoot\iocsimple</span></tt>).</p>
<p>Run ProcServer like so:</p>
<pre class="literal-block">
procserv -e ..\..\bin\windows-x64\simple.exe -n &quot;Simple IOC&quot; -L log.txt 20000 ./st.cmd
</pre>
<p>This will spawn a blank command window for the IOC.
The parameters explained:</p>
<pre class="literal-block">
-e points to the IOC executable
-n the IOC name for the logging
-L the name of the log file
20000 is the port that ProcServer will run on
</pre>
<p>From another command line it should be possible to use <tt class="docutils literal">caget</tt> to get values from the newly spawned IOC.
<strong>Note</strong>: ProcServer can be started without the IOC being loaded using <tt class="docutils literal"><span class="pre">-w</span></tt>, the IOC can then be started later remotely.</p>
</div>
<div class="section" id="connecting-remotely">
<h2>Connecting remotely</h2>
<p>By default, ProcServer access is restricted to the local host. To enable read-only remote access the <tt class="docutils literal"><span class="pre">-l</span></tt> (small L) parameter needs to be specified with a port number. For example:</p>
<pre class="literal-block">
procserv -e ..\..\bin\windows-x64\simple.exe -n &quot;Simple IOC&quot; -L log.txt -l 20001 20000 ./st.cmd
</pre>
<p>Note: the remote access port needs to be opened in the firewall.</p>
<p>Using telnet via PuTTY or similar connect to the appropriate IP address and port, this will lead to something like the following:</p>
<pre class="literal-block">
&#64;&#64;&#64; procServ server PID: 7424
&#64;&#64;&#64; Server startup directory: /cygdrive/c/EPICS_PILOT/ISIS/simpleioc/iocBoot/iocsimple
&#64;&#64;&#64; Child startup directory: /cygdrive/c/EPICS_PILOT/ISIS/simpleioc/iocBoot/iocsimple
&#64;&#64;&#64; Child &quot;Simple IOC&quot; started as: ./st.cmd
&#64;&#64;&#64; Child &quot;Simple IOC&quot; PID: 2152
&#64;&#64;&#64; procServ server started at: Thu Apr  4 11:34:24 2013
&#64;&#64;&#64; Child &quot;Simple IOC&quot; started at: Thu Apr  4 11:34:24 2013
</pre>
<p>The <tt class="docutils literal">&#64;&#64;&#64;</tt> indicates that the message is generated by ProcServer.</p>
<p>To enable remote read/write the <tt class="docutils literal"><span class="pre">--allow</span></tt> parameter must be passed in to the !ProcServer startup. For example:</p>
<pre class="literal-block">
procserv -e ..\..\bin\windows-x64\simple.exe --allow -n &quot;Simple IOC&quot; -L log.txt 20000 ./st.cmd
</pre>
<p>Note: the port (in this case 20000) needs access through the firewall.</p>
<p>Connecting now will show slightly more information:</p>
<pre class="literal-block">
&#64;&#64;&#64; Welcome to procServ (procServ Process Server 2.6.0)
&#64;&#64;&#64; Use ^X to kill the child, auto restart is ON, use ^T to toggle auto restart
&#64;&#64;&#64; procServ server PID: 4748
&#64;&#64;&#64; Server startup directory: /cygdrive/c/EPICS_PILOT/ISIS/simpleioc/iocBoot/iocsimple
&#64;&#64;&#64; Child startup directory: /cygdrive/c/EPICS_PILOT/ISIS/simpleioc/iocBoot/iocsimple
&#64;&#64;&#64; Child &quot;Simple IOC&quot; started as: ./st.cmd
&#64;&#64;&#64; Child &quot;Simple IOC&quot; PID: 6252
&#64;&#64;&#64; procServ server started at: Thu Apr  4 10:52:40 2013
&#64;&#64;&#64; Child &quot;Simple IOC&quot; started at: Thu Apr  4 10:52:40 2013
&#64;&#64;&#64; 0 user(s) and 0 logger(s) connected (plus you)
</pre>
<p>This connection is read/write so sending IOC commands like <tt class="docutils literal">dbl</tt> and <tt class="docutils literal">dbtpf</tt> will work.</p>
<p>By default, typing exit and pressing return will quit and restart the IOC, and a mixture of ProcServer and IOC messages will be seen. The IOC can be set to not automatically restart by specifying the <tt class="docutils literal"><span class="pre">--noautorestart</span></tt> parameter when starting !ProcServer. It is still possible to restart the IOC remotely once exited by using <tt class="docutils literal">CTRL+X</tt> followed by pressing return.</p>
</div>
</div>
<div class="section" id="pv-gateway">
<h1>PV Gateway</h1>
<div class="section" id="building">
<h2>Building</h2>
<p>NOTE: this has already been done for the EPICS PILOT, so it can be downloaded and built from there.</p>
<p>Download <tt class="docutils literal">gnuregex</tt> from EPICS site.
Place in extensionssrc directory (assuming extensions_top has already been installed).</p>
<p>Download gateway source source from EPICS site.
Place in <tt class="docutils literal">extensions\src</tt> directory.</p>
<p>Edit <tt class="docutils literal">gateway.cc</tt> by adding the following near the top:</p>
<pre class="literal-block">
#ifdef WIN32
  #define strcasecmp _stricmp
#endif
</pre>
<p>Edit gateResources.cc and edit line 55 to read:</p>
<pre class="literal-block">
time_t now;
</pre>
<p>Edit line 117 in the Makefile in srcgateway to read:</p>
<pre class="literal-block">
PROD_LIBS = regex
</pre>
<p>Move to the extensions directory and type &quot;make&quot; to build it.</p>
</div>
<div class="section" id="a-simple-example">
<h2>A simple example</h2>
<p>Three machines:</p>
<ul class="simple">
<li>INST = PC running IOCs</li>
<li>GATE = PC running gateway</li>
<li>VIEW = Viewing PC (only needs caget)</li>
</ul>
<div class="figure align-center">
<img alt="Gateway" src="img/misc/gateway.png" style="width: 100%;" />
</div>
<p>The gateway uses a file called <tt class="docutils literal">gateway.pvlist</tt> that defines the PVs available via the gateway; using your PV names, edit it so it contains something along the lines of:</p>
<pre class="literal-block">
PCA:KITNAME:PV1 ALLOW
PCA:KITNAME:PV2 ALLOW
</pre>
<p>IMPORTANT: there must be a blank line after the final definition or it will not work!</p>
<p>There is a second file called gateway.access that defines the access rights. The access is defined using the EPICS Access Security syntax. For read-only access for everyone it should contain:</p>
<pre class="literal-block">
ASG(DEFAULT) {
   RULE(1,READ)
}
</pre>
<p>For more information, see [wiki:AccessSecurity EPICS Access Security]</p>
<p>Start the gateway with the following command (replacing IP_OF_INST and IP_OF_GATE with the correct IP addresses):</p>
<pre class="literal-block">
gateway -pvlist gateway.pvlist -access gateway.access -cip IP_OF_INST -sip IP_OF_GATE
</pre>
<p>NOTE: to send multiple client addresses, use a quoted space separated list, e.g. <tt class="docutils literal">192.168.0.1 192.168.0.2</tt> \
NOTE: if <tt class="docutils literal"><span class="pre">-cip</span></tt> is not defined then the gateway will use <tt class="docutils literal">EPICS_CA_ADDR_LIST</tt> by default. \</p>
<p>On VIEW, run the following commands:</p>
<pre class="literal-block">
set EPICS_CA_ADDR_LIST= IP_OF_GATE
caget PCA:KITNAME:PV1
</pre>
<p>Hopefully, that should work. If you now stop the gateway process on GATE and retry the <tt class="docutils literal">caget</tt> on VIEW, it should fail.</p>
<p>To use an aliases, simply change the <tt class="docutils literal">gateway.pvlist</tt>, so it contains something like:</p>
<pre class="literal-block">
MY_ALIASNAME ALIAS PCA:KITNAME:PV1
</pre>
<p>IMPORTANT: there must be a blank line after the final definition or it will not be defined!</p>
<p>From VIEW, it should now be possible to use <tt class="docutils literal">caget</tt> with the alias:</p>
<pre class="literal-block">
caget MY_ALIASNAME
</pre>
<p>To access statistics about the gateway via Channel Access the <tt class="docutils literal">gateway.pvlist</tt> needs to be edited to allow access to the gateway PVs:</p>
<pre class="literal-block">
PCA:KITNAME:PV1 ALLOW
PCA:KITNAME:PV2 ALLOW
YOURMACHINE.* ALLOW
</pre>
<p>The PVs should now be accessible like so:</p>
<pre class="literal-block">
caget YOURMACHINE:pvtotal
</pre>
</div>
<div class="section" id="running-on-one-machine-block-server">
<h2>Running on one machine (Block Server)</h2>
<div class="section" id="ioc">
<h3>IOC</h3>
<pre class="literal-block">
set EPICS_CA_ADDR_LIST=127.0.0.1 YOUR_IP_ADDRESS
</pre>
<p>Run the SimpleIoc!</p>
</div>
<div class="section" id="gateway">
<h3>Gateway</h3>
<p>Create a file called <tt class="docutils literal">blocks.pvlist</tt> and add the following:</p>
<pre class="literal-block">
BLOCK1 ALIAS NDWxxx:username:SIMPLE:VALUE1
&lt;BLANK LINE&gt;
</pre>
<p>Create a file called gateway.access and add the following:</p>
<pre class="literal-block">
ASG(DEFAULT) {
   RULE(1,READ)
}
</pre>
<pre class="literal-block">
gateway -pvlist blocks.pvlist -access gateway.access -cip 127.0.0.1 -sip YOUR_IP_ADDRESS
</pre>
</div>
<div class="section" id="caget">
<h3>CAGET</h3>
<pre class="literal-block">
set EPICS_CA_ADDR_LIST=127.0.0.1 YOUR_IP_ADDRESS
caget BLOCK1  #This works via the gateway
caget NDWxxx:username:SIMPLE:VALUE1  #This works via standard CA
caput NDWxxx:username:SIMPLE:VALUE1 5  #This works via standard CA
caput BLOCK1 10  #This is not allowed by the gateway
</pre>
</div>
</div>
<div class="section" id="creating-an-alias-gateway">
<h2>Creating an Alias Gateway</h2>
<p>An alias gateway offers three advantages:</p>
<ul class="simple">
<li>It allows access to multiple IOCs running on a single host, regardless of which starts first.</li>
<li>Firewall rules are required only for a single process using known ports</li>
<li>It offers a single place to impose security</li>
</ul>
<p>In order to prevent the gateway from blocking itself, it needs to be run on a different interface or port from the IOCs it is serving.</p>
<p>To use a different port, start gateway with the options <tt class="docutils literal"><span class="pre">-sport</span> 5066 <span class="pre">-cport</span> 5064</tt> and on the client use <tt class="docutils literal">set EPICS_CA_ADDR_LIST=130.246.37.143:5066</tt></p>
<p>We however are planning to restrict the IOCs to running on the loopback interface by setting:</p>
<pre class="literal-block">
set EPICS_CA_ADDR_LIST=127.255.255.255
set EPICS_CAS_BEACON_ADDR_LIST=127.255.255.255
set EPICS_CAS_INTF_ADDR_LIST=127.0.0.1
</pre>
<p>Note that for multiple IOCs to work, the broadcast address must be used.</p>
<p>Because the clients only use the loopback interface they have no interaction with windows firewall.</p>
<p>The gateway can then be started with:</p>
<pre class="literal-block">
gateway.exe -pvlist pvlist.txt -access access.txt -prefix HOST:gateway -cip 127.255.255.255 -sip 130.246.37.143
</pre>
<p>Since it listens only on the external address and looks for PVs only on the loopback address, there is no need for aliasing for non-standard ports to prevent ambiguity.</p>
<p>Assuming the PVs all start HOST:user, the following <tt class="docutils literal">pvlist.txt</tt> will allow full access to any PV, along with the gateway's internal PVs:</p>
<pre class="literal-block">
EVALUATION    ORDER ALLOW, DENY
HOST:gateway:.*    ALLOW
HOST:user:.*    ALLOW    DEFAULT 0
HOST:user:.*    ALLOW    DEFAULT 1
</pre>
<p>The following access.txt allows full access to everything that does not have a group set:</p>
<pre class="literal-block">
ASG(DEFAULT) {
    RULE(0,WRITE)
    RULE(1,WRITE)
}
</pre>
<p>The HOST firewall needs either to allow network access for the gateway program,
or rules like:</p>
<pre class="literal-block">
netsh advfirewall firewall add rule name=&quot;EPICS&quot; dir=in localport=5064 action=allow protocol=udp
netsh advfirewall firewall add rule name=&quot;EPICS&quot; dir=in localport=5064 action=allow protocol=tcp
</pre>
<p>Clients need to point at the correct host:</p>
<pre class="literal-block">
set EPICS_CA_ADDR_LIST=130.246.37.143
</pre>
<p>Any request for a PV starting HOST:user will then be received by the gateway and it will access the IOC.</p>
</div>
</div>
<div class="section" id="epics-access-security">
<h1>EPICS Access Security</h1>
<p>See the  <a class="reference external" href="http://www.aps.anl.gov/epics/base/R3-15/0-docs/AppDevGuide/node9.html#SECTION00910000000000000000">EPICS Application Developer's Guide</a> for more information.</p>
<p>All examples assume you are using the [wiki:CreateSimpleIOC Simple IOC] or something similar.</p>
<div class="section" id="simple-example">
<h2>Simple Example</h2>
<pre class="literal-block">
UAG(uag) {user1, user2}
HAG(hag) {officePC, instPC}
ASG(DEFAULT) {
  RULE(1,READ)
  RULE(1,WRITE) {
    UAG(uag)
    HAG(hag)
  }
}
</pre>
<p>These rules provide read access to anyone located anywhere and write access to user1 and user2 if they are located at officePC or instPC.</p>
<p>The <tt class="docutils literal">1</tt> in <tt class="docutils literal">RULE(1,READ)</tt> represents the access level for a field and must be set to 0 or 1. By default, the standard records types are all defined as 1 except for <tt class="docutils literal">VAL</tt>, <tt class="docutils literal">CMD</tt> and <tt class="docutils literal">RES</tt>. For example: it could be configured that everybody can read record fields with 0 access level, and advanced users can read everything:</p>
<pre class="literal-block">
RULE(0,READ)
RULE(1,READ) {
  UAG(uag)
}
</pre>
<p>Having level 1 access automatically includes access to level 0.</p>
<p>To enable security on an IOC, the following needs to be added before iocInit:</p>
<pre class="literal-block">
asSetFilename(&quot;C:\absolute_path_to_ioc\iocBoot\iocsimple\security.acf&quot;)
</pre>
<p>An absolute file path for the security file should be used.</p>
</div>
<div class="section" id="advanced-example">
<h2>Advanced Example</h2>
<pre class="literal-block">
UAG(local) {user1}
HAG(cabin) {instPC}
UAG(remote) {user2}
HAG(office) {officePC}
ASG(DEFAULT) {
  INPA(simple:value2)
  RULE(1,READ)
  RULE(1,WRITE) {
    UAG(local)
    HAG(cabin)
  }
  RULE(1,WRITE) {
    UAG(remote)
    HAG(office)
    CALC(&quot;A=1&quot;)
  }
}
</pre>
<p>This rule states that:</p>
<blockquote>
<ul class="simple">
<li>everyone can read the PVs</li>
<li>user1 can write to PVs from instPC only</li>
<li>user2 can write to PVs from his office PC, but only if simple:value2 equals 1</li>
</ul>
</blockquote>
</div>
<div class="section" id="access-security-groups">
<h2>Access Security Groups</h2>
<p>A record can be added to a specific access security group using the ASG field, otherwise it will be automatically placed in the DEFAULT ASG.
For example, the following adds the simple:value2 record to the ACCESS ASG:</p>
<pre class="literal-block">
record(ai, &quot;simple:value2&quot;)
{
    field(ASG, &quot;ACCESS&quot;)
    field(VAL, 2)
}
</pre>
<p>The ACCESS group can then have different security settings to the DEFAULT group.
For example, modifying the security file like so:</p>
<pre class="literal-block">
UAG(local) {user1}
HAG(cabin) {instPC}
UAG(remote) {user2}
HAG(office) {officePC}
ASG(DEFAULT) {
  INPA(simple:value2)
  RULE(1,READ)
  RULE(1,WRITE) {
    UAG(local)
    HAG(cabin)
  }
  RULE(1,WRITE) {
    UAG(remote)
    HAG(office)
    CALC(&quot;A=1&quot;)
  }
}
ASG(ACCESS) {
  RULE(1,WRITE) {
    UAG(local)
    HAG(cabin)
  }
}
</pre>
<p>Now only user1 (on instPC) can read or write to <tt class="docutils literal">simple:value2</tt>.</p>
</div>
<div class="section" id="changing-permissions-example">
<h2>Changing Permissions Example</h2>
<p>There are two subroutines (asSubInit, asSubProcess) that can be used to force the IOC to reload the security settings file.
In the .db file add a record like this:</p>
<pre class="literal-block">
record(sub,&quot;reset&quot;) {
   field(INAM,&quot;asSubInit&quot;)
   field(SNAM, &quot;asSubProcess&quot;)
}
</pre>
<p>Set the security file to look something like (change the UAG and HAG details to match your system):</p>
<pre class="literal-block">
UAG(user) {user1}
HAG(office) {officePC}
ASG(DEFAULT) {
  RULE(0,READ)
  RULE(1,WRITE) {
     UAG(user)
     HAG(office)
  }
}
</pre>
<p>Test that it is possible to write to one of the PVs using <tt class="docutils literal">caget</tt>. Next manually remove the write rule from the security file and save it.
Type the following:</p>
<pre class="literal-block">
caget reset 1
</pre>
<p>The security settings should now have been reloaded, and it should no longer be possible to write to any of the PVs (including resetting the permissions!).</p>
</div>
</div>
<div class="section" id="using-the-array-subroutine-asub">
<h1>Using the Array Subroutine (aSub)</h1>
<p>An aSub record is a record that can call a C routine. This record is not used for device communication.</p>
<div class="section" id="creating-an-ioc-that-uses-asub">
<h2>Creating an IOC that uses aSub</h2>
<p>A simple example that creates an aSub record that doubles the input value.</p>
<p>Create an IOC in the usual method:</p>
<pre class="literal-block">
makeBaseApp.pl -t ioc asubtest
makeBaseApp.pl -i -t ioc asubtest
</pre>
<p>Move to the <tt class="docutils literal">asubtestApp\src</tt> directory and create a file called <tt class="docutils literal">my_asub_routine.c</tt>.
In the new file put (warning: bad C code alert):</p>
<pre class="literal-block">
#include &lt;registryFunction.h&gt;
#include &lt;epicsExport.h&gt;
#include &quot;aSubRecord.h&quot;
#include &quot;stdlib.h&quot;
static long my_asub_routine(aSubRecord *prec) {
    long i;
    double *a, *vala;
    prec-&gt;pact = 1;
    //Note: may be an array
    a = (double *)prec-&gt;a;
    for(i=0; i &lt; prec-&gt;noa; ++i)
    {
        ((double *)prec-&gt;vala)[i] = a[i] * 2.0f;
    }
    prec-&gt;pact = 0;
    //Debug message - prints to IOC
    //printf(&quot;my_asub_routine called&quot;);
    return 0;
}
epicsRegisterFunction(my_asub_routine);
</pre>
<p>Create a file called asubroutine.dbd and put the following in it:</p>
<pre class="literal-block">
function(my_asub_routine)
</pre>
<p>Open the Makefile, and add the following in the appropriate places:</p>
<pre class="literal-block">
asubtest_DBD += asubroutine.dbd
asubtest_SRCS += my_asub_routine.c
</pre>
<p>Move to the <tt class="docutils literal">asubtestApp\Db</tt> directory and create a file called <tt class="docutils literal">asubtest.db</tt>.
Add the following to it:</p>
<pre class="literal-block">
record(ai, &quot;testasub:value_in&quot;)
{
    field(VAL, 1)
    field(FLNK,&quot;testasub:my_asub&quot;)
}
record(aSub,&quot;testasub:my_asub&quot;)
{
    field(SNAM,&quot;my_asub_routine&quot;)
    field(FTA, &quot;DOUBLE&quot;)
    field(INPA, &quot;testasub:value_in&quot;)
    field (OUTA, &quot;testasub:value_out&quot;)
    field (FTVA, &quot;DOUBLE&quot;)
}
record(ai, &quot;testasub:value_out&quot;)
{
    field(INP, &quot;testasub:my_asub.VALA&quot;)
}
</pre>
<p>Return to the IOC's top directory and run make.
Assuming it builds successfully, run the IOC and from another command-line try:</p>
<pre class="literal-block">
caput testasub:value_in 5
</pre>
<p>Followed by:</p>
<pre class="literal-block">
caget testasub:value_out
</pre>
<p>The <tt class="docutils literal">caget</tt> should return a value of 10.</p>
<p>NOTE: The <tt class="docutils literal">aSub</tt> record automatically allocates space for input and output values based on NOA and NOVA.</p>
</div>
</div>
<div class="section" id="adding-deviocstats-to-an-ioc">
<h1>Adding devIocStats to an IOC</h1>
<p>Assuming devIocStats exists in your system and the IOC to be modified is complete (i.e. it builds and runs correctly), follow the following steps to add devIocStats to it:</p>
<ul class="simple">
<li>Open <tt class="docutils literal">configure\RELEASE</tt> and add <tt class="docutils literal"><span class="pre">DEVIOCSTATS=YOUR_PATH/devIocStats/3-1-11</span></tt> with <tt class="docutils literal">YOUR_PATH</tt> replaced appropriately.</li>
<li>Open the <tt class="docutils literal">st.cmd</tt> for the IOC and change it to look something like this</li>
</ul>
<pre class="literal-block">
#!../../bin/windows-x64/MY_IOC
## You may have to change MY_IOC to something else
## everywhere it appears in this file
&lt; envPaths
epicsEnvSet &quot;IOCNAME&quot; &quot;$(P=$(MYPVPREFIX))MY_IOC&quot;               ## (1) The IOC name used in PVs
epicsEnvSet &quot;IOCSTATS_DB&quot; &quot;$(DEVIOCSTATS)/db/iocAdminSoft.db&quot;  ## (2) The path to devIocStats db to use
cd ${TOP}
## Register all support components
dbLoadDatabase &quot;dbd/MY_IOC.dbd&quot;
MY_IOC_registerRecordDeviceDriver pdbbase
dbLoadRecords(&quot;db/my_ioc.db&quot;,&quot;P=$(IOCNAME)&quot;)                   ## (3) Pass the IOCNAME to the IOC's db
dbLoadRecords(&quot;$(IOCSTATS_DB)&quot;,&quot;IOC=$(IOCNAME)&quot;)               ## (4) Load the devIocStats db
cd ${TOP}/iocBoot/${IOC}
iocInit
</pre>
<p>The key changes are highlighted by the numbered comments.</p>
<ul>
<li><p class="first">Open <tt class="docutils literal">MY_IOCApp\src\Makefile</tt> and add:</p>
<pre class="literal-block">
MY_IOC_DBD += devIocStats.dbd
MY_IOC_LIBS += devIocStats
</pre>
</li>
</ul>
<p><strong>Additional step</strong>: if there is a dbd file in <tt class="docutils literal">MY_IOCApp\src</tt>, then you might need to add <tt class="docutils literal">include &quot;devIocStats.dbd&quot;</tt> to it.</p>
<p>Finally rebuild the IOC (<tt class="docutils literal">make clean uninstall</tt> followed by <tt class="docutils literal">make</tt>)</p>
</div>
<div class="section" id="creating-a-sequencer">
<h1>Creating a Sequencer</h1>
<div class="section" id="create-an-ioc">
<h2>Create an IOC</h2>
<pre class="literal-block">
mkdir seqex
cd seqex
makebaseapp.pl -t ioc seqex
makebaseapp.pl -i -t ioc seqex
</pre>
</div>
<div class="section" id="create-additional-files">
<h2>Create additional files</h2>
<pre class="literal-block">
cd seqexApp/db
echo. 2&gt; seqex.db
cd ..
cd src
echo. 2&gt; sncProgram.st
echo. 2&gt; sncExample.stt
echo. 2&gt; sncExample.dbd
</pre>
</div>
<div class="section" id="modify-the-files">
<h2>Modify the files</h2>
<p><strong>seqexApp/db/seqex.db</strong></p>
<pre class="literal-block">
record(ai, &quot;$(user):aiExample&quot;)
{
        field(DESC, &quot;Analog input&quot;)
        field(INP, &quot;$(user):calcExample.VAL  NPP NMS&quot;)
        field(EGUF, &quot;10&quot;)
        field(EGU, &quot;Counts&quot;)
        field(HOPR, &quot;10&quot;)
        field(LOPR, &quot;0&quot;)
        field(HIHI, &quot;8&quot;)
        field(HIGH, &quot;6&quot;)
        field(LOW, &quot;4&quot;)
        field(LOLO, &quot;2&quot;)
        field(HHSV, &quot;MAJOR&quot;)
        field(HSV, &quot;MINOR&quot;)
        field(LSV, &quot;MINOR&quot;)
        field(LLSV, &quot;MAJOR&quot;)
}
record(calc, &quot;$(user):calcExample&quot;)
{
        field(DESC, &quot;Counter&quot;)
        field(SCAN,&quot;1 second&quot;)
        field(FLNK, &quot;$(user):aiExample&quot;)
        field(CALC, &quot;(A&lt;B)?(A+C):D&quot;)
        field(INPA, &quot;$(user):calcExample.VAL  NPP NMS&quot;)
        field(INPB, &quot;9&quot;)
        field(INPC, &quot;1&quot;)
        field(INPD, &quot;0&quot;)
        field(EGU, &quot;Counts&quot;)
        field(HOPR, &quot;10&quot;)
        field(HIHI, &quot;8&quot;)
        field(HIGH, &quot;6&quot;)
        field(LOW, &quot;4&quot;)
        field(LOLO, &quot;2&quot;)
        field(HHSV, &quot;MAJOR&quot;)
        field(HSV, &quot;MINOR&quot;)
        field(LSV, &quot;MINOR&quot;)
        field(LLSV, &quot;MAJOR&quot;)
}
</pre>
<p><strong>seqexApp/db/Makefile</strong></p>
<p>Add:</p>
<pre class="literal-block">
DB += seqex.db
</pre>
<p><strong>seqexApp/src/sncProgram.st</strong></p>
<pre class="literal-block">
#include &quot;../sncExample.stt&quot;
</pre>
<p><strong>seqexApp/src/sncExample.stt</strong></p>
<pre class="literal-block">
program sncExample
double v;
assign v to &quot;{user}:aiExample&quot;;
monitor v;
ss ss1 {
        state init {
        when (delay(10)) {
                printf(&quot;sncExample: Startup delay over\n&quot;);
        } state low
        }
        state low {
        when (v &gt; 5.0) {
                printf(&quot;sncExample: Changing to high\n&quot;);
        } state high
        }
        state high {
        when (v &lt;= 5.0) {
                printf(&quot;sncExample: Changing to low\n&quot;);
        } state low
        }
}
</pre>
<p><strong>seqexApp/src/sncExample.dbd</strong></p>
<blockquote>
registrar(sncExampleRegistrar)</blockquote>
<p><strong>build.mak (if using ISIS build) or Makefile (if not)</strong>
Add:</p>
<pre class="literal-block">
ifneq ($(SNCSEQ),)
        # Build sncExample
        sncExample_SNCFLAGS += +r
        $(APPNAME)_DBD += sncExample.dbd
        $(APPNAME)_SRCS += sncExample.stt
        $(APPNAME)_LIBS += seq pv
endif
</pre>
<p><strong>configure/RELEASE</strong>
Make sure there is a uncommented line like below but with the correct path for your system:</p>
<pre class="literal-block">
SNCSEQ=PATH_TO_YOUR_SEQ_INSTALLATION
</pre>
<p><strong>iocBoot/iocseqex/st.cmd</strong>
Uncomment and adjust the dbLoadrecords line, e.g:</p>
<pre class="literal-block">
## Load our record instances
dbLoadRecords(&quot;db/seqex.db&quot;,&quot;user=yournameHost&quot;)
</pre>
<p>Uncomment and adjust the seq line, e.g.:</p>
<pre class="literal-block">
## Start any sequence programs
seq sncExample,&quot;user=yourname3Host&quot;
</pre>
</div>
<div class="section" id="build-the-ioc">
<h2>Build the IOC</h2>
<p>Build and run the IOC as normal.</p>
</div>
</div>
</div>

      </div>
      <div id="anydiff">
        <form action="/EPICS/diff" method="get">
          <div class="buttons">
            <input type="hidden" name="new_path" value="/trunk/isisdoc/misc_docs/EPICS_basics.rst" />
            <input type="hidden" name="old_path" value="/trunk/isisdoc/misc_docs/EPICS_basics.rst" />
            <input type="hidden" name="new_rev" />
            <input type="hidden" name="old_rev" />
            <input type="submit" value="View changes..." title="Select paths and revs for diff" />
          </div>
        </form>
      </div>
      <div id="help"><strong>Note:</strong> See <a href="/EPICS/wiki/TracBrowser">TracBrowser</a> for help on using the repository browser.</div>
    </div>
    <div id="altlinks">
      <h3>Download in other formats:</h3>
      <ul>
        <li class="first">
          <a rel="nofollow" href="/EPICS/browser/trunk/isisdoc/misc_docs/EPICS_basics.rst?format=txt">Plain text</a>
        </li><li class="last">
          <a rel="nofollow" href="/EPICS/export/3115/trunk/isisdoc/misc_docs/EPICS_basics.rst">Original format</a>
        </li>
      </ul>
    </div>
    </div>
    <div id="footer" lang="en" xml:lang="en"><hr />
      <a id="tracpowered" href="http://trac.edgewall.org/"><img src="/EPICS/chrome/common/trac_logo_mini.png" height="30" width="107" alt="Trac Powered" /></a>
      <p class="left">Powered by <a href="/EPICS/about"><strong>Trac 1.0.8</strong></a><br />
        By <a href="http://www.edgewall.org/">Edgewall Software</a>.</p>
      <p class="right">Visit the Trac open source project at<br /><a href="http://trac.edgewall.org/">http://trac.edgewall.org/</a></p>
    </div>
  </body>
</html>