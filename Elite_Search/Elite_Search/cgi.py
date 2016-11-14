<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en-US">
<head>
<link rel="icon" href="/cpython/static/hgicon.png" type="image/png" />
<meta name="robots" content="index, nofollow" />
<link rel="stylesheet" href="/cpython/static/style-paper.css" type="text/css" />
<script type="text/javascript" src="/cpython/static/mercurial.js"></script>

<link rel="stylesheet" href="/cpython/highlightcss" type="text/css" />
<title>cpython: 9db5846f126d Lib/cgi.py</title>
</head>
<body>

<div class="container">
<div class="menu">
<div class="logo">
<a href="https://hg.python.org">
<img src="/cpython/static/hglogo.png" alt="back to hg.python.org repositories" /></a>
</div>
<ul>
<li><a href="/cpython/shortlog/2.7">log</a></li>
<li><a href="/cpython/graph/2.7">graph</a></li>
<li><a href="/cpython/tags">tags</a></li>
<li><a href="/cpython/bookmarks">bookmarks</a></li>
<li><a href="/cpython/branche" \
            "s">branches</a></li>
</ul>
<ul>
<li><a href="/cpython/rev/2.7">changeset</a></li>
<li><a href="/cpython/file/2.7/Lib/">browse</a></li>
</ul>
<ul>
<li class="active">file</li>
<li><a href="/cpython/file/tip/Lib/cgi.py">latest</a></li>
<li><a href="/cpython/diff/2.7/Lib/cgi.py">diff</a></li>
<li><a href="/cpython/comparison/2.7/Lib/cgi.py">comparison</a></li>
<li><a href="/cpython/annotate/2.7/Lib/cgi.py">annotate</a></li>
<li><a href="/cpython/log/2.7/Lib/cgi.py">file log</a></li>
<li><a href="/cpython/raw-file/2.7/Lib/cgi.py">raw</a></li>
</ul>
<ul>
<li><a href="/cpython/help">help</a></li>
</ul>
</div>

<div class="main">
<h2 class="breadcrumb"><a href="/">Mercurial</a> &gt; <a href="/cpython">cpython</a> </h2>
<h3>
 view Lib/cgi.py @ 100502:<a href="/cpython/rev/9db5846f126d">9db5846f126d</a>
 <span class="branchname">2.7</span> 
</h3>

<form class="search" action="/cpython/log">

<p><input name="rev" id="search1" type="text" size="30" /></p>
<div id="hint">Find changesets by keywords (author, files, the commit message), revision
number or hash, or <a href="/cpython/help/revsets">revset expression</a>.</div>
</form>

<div class="description">Issue #26513: Fixes platform module detection of Windows Server</a> [<a href="http://bugs.python.org/26513" class="issuelink">#26513</a>]</div>

<table id="changesetEntry">
<tr>
 <th class="author">author</th>
 <td class="author">&#83;&#116;&#101;&#118;&#101;&#32;&#68;&#111;&#119;&#101;&#114;&#32;&#60;&#115;&#116;&#101;&#118;&#101;&#46;&#100;&#111;&#119;&#101;&#114;&#64;&#109;&#105;&#99;&#114;&#111;&#115;&#111;&#102;&#116;&#46;&#99;&#111;&#109;&#62;</td>
</tr>
<tr>
 <th class="date">date</th>
 <td class="date age">Sat, 12 Mar 2016 08:07:04 -0800</td>
</tr>
<tr>
 <th class="author">parents</th>
 <td class="author"><a href="/cpython/file/63058453a4cc/Lib/cgi.py">63058453a4cc</a> </td>
</tr>
<tr>
 <th class="author">children</th>
 <td class="author"></td>
</tr>
</table>

<div class="overflow">
<div class="sourcefirst linewraptoggle">line wrap: <a class="linewraplink" href="javascript:toggleLinewrap()">on</a></div>
<div class="sourcefirst"> line source</div>
<pre class="sourcelines stripes4 wrap">
<span id="l1"><span class="c">#! /usr/local/bin/python</span></span><a href="#l1"></a>
<span id="l2"></span><a href="#l2"></a>
<span id="l3"><span class="c"># NOTE: the above &quot;/usr/local/bin/python&quot; is NOT a mistake.  It is</span></span><a href="#l3"></a>
<span id="l4"><span class="c"># intentionally NOT &quot;/usr/bin/env python&quot;.  On many systems</span></span><a href="#l4"></a>
<span id="l5"><span class="c"># (e.g. Solaris), /usr/local/bin is not in $PATH as passed to CGI</span></span><a href="#l5"></a>
<span id="l6"><span class="c"># scripts, and /usr/local/bin is the default directory where Python is</span></span><a href="#l6"></a>
<span id="l7"><span class="c"># installed, so /usr/bin/env would be unable to find python.  Granted,</span></span><a href="#l7"></a>
<span id="l8"><span class="c"># binary installations by Linux vendors often install Python in</span></span><a href="#l8"></a>
<span id="l9"><span class="c"># /usr/bin.  So let those vendors patch cgi.py to match their choice</span></span><a href="#l9"></a>
<span id="l10"><span class="c"># of installation.</span></span><a href="#l10"></a>
<span id="l11"></span><a href="#l11"></a>
<span id="l12"><span class="sd">&quot;&quot;&quot;Support module for CGI (Common Gateway Interface) scripts.</span></span><a href="#l12"></a>
<span id="l13"></span><a href="#l13"></a>
<span id="l14"><span class="sd">This module defines a number of utilities for use by CGI scripts</span></span><a href="#l14"></a>
<span id="l15"><span class="sd">written in Python.</span></span><a href="#l15"></a>
<span id="l16"><span class="sd">&quot;&quot;&quot;</span></span><a href="#l16"></a>
<span id="l17"></span><a href="#l17"></a>
<span id="l18"><span class="c"># XXX Perhaps there should be a slimmed version that doesn&#39;t contain</span></span><a href="#l18"></a>
<span id="l19"><span class="c"># all those backwards compatible and debugging classes and functions?</span></span><a href="#l19"></a>
<span id="l20"></span><a href="#l20"></a>
<span id="l21"><span class="c"># History</span></span><a href="#l21"></a>
<span id="l22"><span class="c"># -------</span></span><a href="#l22"></a>
<span id="l23"><span class="c">#</span></span><a href="#l23"></a>
<span id="l24"><span class="c"># Michael McLay started this module.  Steve Majewski changed the</span></span><a href="#l24"></a>
<span id="l25"><span class="c"># interface to SvFormContentDict and FormContentDict.  The multipart</span></span><a href="#l25"></a>
<span id="l26"><span class="c"># parsing was inspired by code submitted by Andreas Paepcke.  Guido van</span></span><a href="#l26"></a>
<span id="l27"><span class="c"># Rossum rewrote, reformatted and documented the module and is currently</span></span><a href="#l27"></a>
<span id="l28"><span class="c"># responsible for its maintenance.</span></span><a href="#l28"></a>
<span id="l29"><span class="c">#</span></span><a href="#l29"></a>
<span id="l30"></span><a href="#l30"></a>
<span id="l31"><span class="n">__version__</span> <span class="o">=</span> <span class="s">&quot;2.6&quot;</span></span><a href="#l31"></a>
<span id="l32"></span><a href="#l32"></a>
<span id="l33"></span><a href="#l33"></a>
<span id="l34"><span class="c"># Imports</span></span><a href="#l34"></a>
<span id="l35"><span class="c"># =======</span></span><a href="#l35"></a>
<span id="l36"></span><a href="#l36"></a>
<span id="l37"><span class="kn">from</span> <span class="nn">operator</span> <span class="kn">import</span> <span class="n">attrgetter</span></span><a href="#l37"></a>
<span id="l38"><span class="kn">import</span> <span class="nn">sys</span></span><a href="#l38"></a>
<span id="l39"><span class="kn">import</span> <span class="nn">os</span></span><a href="#l39"></a>
<span id="l40"><span class="kn">import</span> <span class="nn">UserDict</span></span><a href="#l40"></a>
<span id="l41"><span class="kn">import</span> <span class="nn">urlparse</span></span><a href="#l41"></a>
<span id="l42"></span><a href="#l42"></a>
<span id="l43"><span class="kn">from</span> <span class="nn">warnings</span> <span class="kn">import</span> <span class="n">filterwarnings</span><span class="p">,</span> <span class="n">catch_warnings</span><span class="p">,</span> <span class="n">warn</span></span><a href="#l43"></a>
<span id="l44"><span class="k">with</span> <span class="n">catch_warnings</span><span class="p">():</span></span><a href="#l44"></a>
<span id="l45">    <span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">py3kwarning</span><span class="p">:</span></span><a href="#l45"></a>
<span id="l46">        <span class="n">filterwarnings</span><span class="p">(</span><span class="s">&quot;ignore&quot;</span><span class="p">,</span> <span class="s">&quot;.*mimetools has been removed&quot;</span><span class="p">,</span></span><a href="#l46"></a>
<span id="l47">                       <span class="ne">DeprecationWarning</span><span class="p">)</span></span><a href="#l47"></a>
<span id="l48">        <span class="n">filterwarnings</span><span class="p">(</span><span class="s">&quot;ignore&quot;</span><span class="p">,</span> <span class="s">&quot;.*rfc822 has been removed&quot;</span><span class="p">,</span></span><a href="#l48"></a>
<span id="l49">                       <span class="ne">DeprecationWarning</span><span class="p">)</span></span><a href="#l49"></a>
<span id="l50">    <span class="kn">import</span> <span class="nn">mimetools</span></span><a href="#l50"></a>
<span id="l51">    <span class="kn">import</span> <span class="nn">rfc822</span></span><a href="#l51"></a>
<span id="l52"></span><a href="#l52"></a>
<span id="l53"><span class="k">try</span><span class="p">:</span></span><a href="#l53"></a>
<span id="l54">    <span class="kn">from</span> <span class="nn">cStringIO</span> <span class="kn">import</span> <span class="n">StringIO</span></span><a href="#l54"></a>
<span id="l55"><span class="k">except</span> <span class="ne">ImportError</span><span class="p">:</span></span><a href="#l55"></a>
<span id="l56">    <span class="kn">from</span> <span class="nn">StringIO</span> <span class="kn">import</span> <span class="n">StringIO</span></span><a href="#l56"></a>
<span id="l57"></span><a href="#l57"></a>
<span id="l58"><span class="n">__all__</span> <span class="o">=</span> <span class="p">[</span><span class="s">&quot;MiniFieldStorage&quot;</span><span class="p">,</span> <span class="s">&quot;FieldStorage&quot;</span><span class="p">,</span> <span class="s">&quot;FormContentDict&quot;</span><span class="p">,</span></span><a href="#l58"></a>
<span id="l59">           <span class="s">&quot;SvFormContentDict&quot;</span><span class="p">,</span> <span class="s">&quot;InterpFormContentDict&quot;</span><span class="p">,</span> <span class="s">&quot;FormContent&quot;</span><span class="p">,</span></span><a href="#l59"></a>
<span id="l60">           <span class="s">&quot;parse&quot;</span><span class="p">,</span> <span class="s">&quot;parse_qs&quot;</span><span class="p">,</span> <span class="s">&quot;parse_qsl&quot;</span><span class="p">,</span> <span class="s">&quot;parse_multipart&quot;</span><span class="p">,</span></span><a href="#l60"></a>
<span id="l61">           <span class="s">&quot;parse_header&quot;</span><span class="p">,</span> <span class="s">&quot;print_exception&quot;</span><span class="p">,</span> <span class="s">&quot;print_environ&quot;</span><span class="p">,</span></span><a href="#l61"></a>
<span id="l62">           <span class="s">&quot;print_form&quot;</span><span class="p">,</span> <span class="s">&quot;print_directory&quot;</span><span class="p">,</span> <span class="s">&quot;print_arguments&quot;</span><span class="p">,</span></span><a href="#l62"></a>
<span id="l63">           <span class="s">&quot;print_environ_usage&quot;</span><span class="p">,</span> <span class="s">&quot;escape&quot;</span><span class="p">]</span></span><a href="#l63"></a>
<span id="l64"></span><a href="#l64"></a>
<span id="l65"><span class="c"># Logging support</span></span><a href="#l65"></a>
<span id="l66"><span class="c"># ===============</span></span><a href="#l66"></a>
<span id="l67"></span><a href="#l67"></a>
<span id="l68"><span class="n">logfile</span> <span class="o">=</span> <span class="s">&quot;&quot;</span>            <span class="c"># Filename to log to, if not empty</span></span><a href="#l68"></a>
<span id="l69"><span class="n">logfp</span> <span class="o">=</span> <span class="bp">None</span>            <span class="c"># File object to log to, if not None</span></span><a href="#l69"></a>
<span id="l70"></span><a href="#l70"></a>
<span id="l71"><span class="k">def</span> <span class="nf">initlog</span><span class="p">(</span><span class="o">*</span><span class="n">allargs</span><span class="p">):</span></span><a href="#l71"></a>
<span id="l72">    <span class="sd">&quot;&quot;&quot;Write a log message, if there is a log file.</span></span><a href="#l72"></a>
<span id="l73"></span><a href="#l73"></a>
<span id="l74"><span class="sd">    Even though this function is called initlog(), you should always</span></span><a href="#l74"></a>
<span id="l75"><span class="sd">    use log(); log is a variable that is set either to initlog</span></span><a href="#l75"></a>
<span id="l76"><span class="sd">    (initially), to dolog (once the log file has been opened), or to</span></span><a href="#l76"></a>
<span id="l77"><span class="sd">    nolog (when logging is disabled).</span></span><a href="#l77"></a>
<span id="l78"></span><a href="#l78"></a>
<span id="l79"><span class="sd">    The first argument is a format string; the remaining arguments (if</span></span><a href="#l79"></a>
<span id="l80"><span class="sd">    any) are arguments to the % operator, so e.g.</span></span><a href="#l80"></a>
<span id="l81"><span class="sd">        log(&quot;%s: %s&quot;, &quot;a&quot;, &quot;b&quot;)</span></span><a href="#l81"></a>
<span id="l82"><span class="sd">    will write &quot;a: b&quot; to the log file, followed by a newline.</span></span><a href="#l82"></a>
<span id="l83"></span><a href="#l83"></a>
<span id="l84"><span class="sd">    If the global logfp is not None, it should be a file object to</span></span><a href="#l84"></a>
<span id="l85"><span class="sd">    which log data is written.</span></span><a href="#l85"></a>
<span id="l86"></span><a href="#l86"></a>
<span id="l87"><span class="sd">    If the global logfp is None, the global logfile may be a string</span></span><a href="#l87"></a>
<span id="l88"><span class="sd">    giving a filename to open, in append mode.  This file should be</span></span><a href="#l88"></a>
<span id="l89"><span class="sd">    world writable!!!  If the file can&#39;t be opened, logging is</span></span><a href="#l89"></a>
<span id="l90"><span class="sd">    silently disabled (since there is no safe place where we could</span></span><a href="#l90"></a>
<span id="l91"><span class="sd">    send an error message).</span></span><a href="#l91"></a>
<span id="l92"></span><a href="#l92"></a>
<span id="l93"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l93"></a>
<span id="l94">    <span class="k">global</span> <span class="n">logfp</span><span class="p">,</span> <span class="n">log</span></span><a href="#l94"></a>
<span id="l95">    <span class="k">if</span> <span class="n">logfile</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">logfp</span><span class="p">:</span></span><a href="#l95"></a>
<span id="l96">        <span class="k">try</span><span class="p">:</span></span><a href="#l96"></a>
<span id="l97">            <span class="n">logfp</span> <span class="o">=</span> <span class="nb">open</span><span class="p">(</span><span class="n">logfile</span><span class="p">,</span> <span class="s">&quot;a&quot;</span><span class="p">)</span></span><a href="#l97"></a>
<span id="l98">        <span class="k">except</span> <span class="ne">IOError</span><span class="p">:</span></span><a href="#l98"></a>
<span id="l99">            <span class="k">pass</span></span><a href="#l99"></a>
<span id="l100">    <span class="k">if</span> <span class="ow">not</span> <span class="n">logfp</span><span class="p">:</span></span><a href="#l100"></a>
<span id="l101">        <span class="n">log</span> <span class="o">=</span> <span class="n">nolog</span></span><a href="#l101"></a>
<span id="l102">    <span class="k">else</span><span class="p">:</span></span><a href="#l102"></a>
<span id="l103">        <span class="n">log</span> <span class="o">=</span> <span class="n">dolog</span></span><a href="#l103"></a>
<span id="l104">    <span class="n">log</span><span class="p">(</span><span class="o">*</span><span class="n">allargs</span><span class="p">)</span></span><a href="#l104"></a>
<span id="l105"></span><a href="#l105"></a>
<span id="l106"><span class="k">def</span> <span class="nf">dolog</span><span class="p">(</span><span class="n">fmt</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">):</span></span><a href="#l106"></a>
<span id="l107">    <span class="sd">&quot;&quot;&quot;Write a log message to the log file.  See initlog() for docs.&quot;&quot;&quot;</span></span><a href="#l107"></a>
<span id="l108">    <span class="n">logfp</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">fmt</span><span class="o">%</span><span class="n">args</span> <span class="o">+</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">)</span></span><a href="#l108"></a>
<span id="l109"></span><a href="#l109"></a>
<span id="l110"><span class="k">def</span> <span class="nf">nolog</span><span class="p">(</span><span class="o">*</span><span class="n">allargs</span><span class="p">):</span></span><a href="#l110"></a>
<span id="l111">    <span class="sd">&quot;&quot;&quot;Dummy function, assigned to log when logging is disabled.&quot;&quot;&quot;</span></span><a href="#l111"></a>
<span id="l112">    <span class="k">pass</span></span><a href="#l112"></a>
<span id="l113"></span><a href="#l113"></a>
<span id="l114"><span class="n">log</span> <span class="o">=</span> <span class="n">initlog</span>           <span class="c"># The current logging function</span></span><a href="#l114"></a>
<span id="l115"></span><a href="#l115"></a>
<span id="l116"></span><a href="#l116"></a>
<span id="l117"><span class="c"># Parsing functions</span></span><a href="#l117"></a>
<span id="l118"><span class="c"># =================</span></span><a href="#l118"></a>
<span id="l119"></span><a href="#l119"></a>
<span id="l120"><span class="c"># Maximum input we will accept when REQUEST_METHOD is POST</span></span><a href="#l120"></a>
<span id="l121"><span class="c"># 0 ==&gt; unlimited input</span></span><a href="#l121"></a>
<span id="l122"><span class="n">maxlen</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l122"></a>
<span id="l123"></span><a href="#l123"></a>
<span id="l124"><span class="k">def</span> <span class="nf">parse</span><span class="p">(</span><span class="n">fp</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">environ</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></span><a href="#l124"></a>
<span id="l125">    <span class="sd">&quot;&quot;&quot;Parse a query in the environment or from a file (default stdin)</span></span><a href="#l125"></a>
<span id="l126"></span><a href="#l126"></a>
<span id="l127"><span class="sd">        Arguments, all optional:</span></span><a href="#l127"></a>
<span id="l128"></span><a href="#l128"></a>
<span id="l129"><span class="sd">        fp              : file pointer; default: sys.stdin</span></span><a href="#l129"></a>
<span id="l130"></span><a href="#l130"></a>
<span id="l131"><span class="sd">        environ         : environment dictionary; default: os.environ</span></span><a href="#l131"></a>
<span id="l132"></span><a href="#l132"></a>
<span id="l133"><span class="sd">        keep_blank_values: flag indicating whether blank values in</span></span><a href="#l133"></a>
<span id="l134"><span class="sd">            percent-encoded forms should be treated as blank strings.</span></span><a href="#l134"></a>
<span id="l135"><span class="sd">            A true value indicates that blanks should be retained as</span></span><a href="#l135"></a>
<span id="l136"><span class="sd">            blank strings.  The default false value indicates that</span></span><a href="#l136"></a>
<span id="l137"><span class="sd">            blank values are to be ignored and treated as if they were</span></span><a href="#l137"></a>
<span id="l138"><span class="sd">            not included.</span></span><a href="#l138"></a>
<span id="l139"></span><a href="#l139"></a>
<span id="l140"><span class="sd">        strict_parsing: flag indicating what to do with parsing errors.</span></span><a href="#l140"></a>
<span id="l141"><span class="sd">            If false (the default), errors are silently ignored.</span></span><a href="#l141"></a>
<span id="l142"><span class="sd">            If true, errors raise a ValueError exception.</span></span><a href="#l142"></a>
<span id="l143"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l143"></a>
<span id="l144">    <span class="k">if</span> <span class="n">fp</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l144"></a>
<span id="l145">        <span class="n">fp</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span></span><a href="#l145"></a>
<span id="l146">    <span class="k">if</span> <span class="ow">not</span> <span class="s">&#39;REQUEST_METHOD&#39;</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span></span><a href="#l146"></a>
<span id="l147">        <span class="n">environ</span><span class="p">[</span><span class="s">&#39;REQUEST_METHOD&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&#39;GET&#39;</span>       <span class="c"># For testing stand-alone</span></span><a href="#l147"></a>
<span id="l148">    <span class="k">if</span> <span class="n">environ</span><span class="p">[</span><span class="s">&#39;REQUEST_METHOD&#39;</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;POST&#39;</span><span class="p">:</span></span><a href="#l148"></a>
<span id="l149">        <span class="n">ctype</span><span class="p">,</span> <span class="n">pdict</span> <span class="o">=</span> <span class="n">parse_header</span><span class="p">(</span><span class="n">environ</span><span class="p">[</span><span class="s">&#39;CONTENT_TYPE&#39;</span><span class="p">])</span></span><a href="#l149"></a>
<span id="l150">        <span class="k">if</span> <span class="n">ctype</span> <span class="o">==</span> <span class="s">&#39;multipart/form-data&#39;</span><span class="p">:</span></span><a href="#l150"></a>
<span id="l151">            <span class="k">return</span> <span class="n">parse_multipart</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="n">pdict</span><span class="p">)</span></span><a href="#l151"></a>
<span id="l152">        <span class="k">elif</span> <span class="n">ctype</span> <span class="o">==</span> <span class="s">&#39;application/x-www-form-urlencoded&#39;</span><span class="p">:</span></span><a href="#l152"></a>
<span id="l153">            <span class="n">clength</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">environ</span><span class="p">[</span><span class="s">&#39;CONTENT_LENGTH&#39;</span><span class="p">])</span></span><a href="#l153"></a>
<span id="l154">            <span class="k">if</span> <span class="n">maxlen</span> <span class="ow">and</span> <span class="n">clength</span> <span class="o">&gt;</span> <span class="n">maxlen</span><span class="p">:</span></span><a href="#l154"></a>
<span id="l155">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">,</span> <span class="s">&#39;Maximum content length exceeded&#39;</span></span><a href="#l155"></a>
<span id="l156">            <span class="n">qs</span> <span class="o">=</span> <span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="n">clength</span><span class="p">)</span></span><a href="#l156"></a>
<span id="l157">        <span class="k">else</span><span class="p">:</span></span><a href="#l157"></a>
<span id="l158">            <span class="n">qs</span> <span class="o">=</span> <span class="s">&#39;&#39;</span>                     <span class="c"># Unknown content-type</span></span><a href="#l158"></a>
<span id="l159">        <span class="k">if</span> <span class="s">&#39;QUERY_STRING&#39;</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span></span><a href="#l159"></a>
<span id="l160">            <span class="k">if</span> <span class="n">qs</span><span class="p">:</span> <span class="n">qs</span> <span class="o">=</span> <span class="n">qs</span> <span class="o">+</span> <span class="s">&#39;&amp;&#39;</span></span><a href="#l160"></a>
<span id="l161">            <span class="n">qs</span> <span class="o">=</span> <span class="n">qs</span> <span class="o">+</span> <span class="n">environ</span><span class="p">[</span><span class="s">&#39;QUERY_STRING&#39;</span><span class="p">]</span></span><a href="#l161"></a>
<span id="l162">        <span class="k">elif</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]:</span></span><a href="#l162"></a>
<span id="l163">            <span class="k">if</span> <span class="n">qs</span><span class="p">:</span> <span class="n">qs</span> <span class="o">=</span> <span class="n">qs</span> <span class="o">+</span> <span class="s">&#39;&amp;&#39;</span></span><a href="#l163"></a>
<span id="l164">            <span class="n">qs</span> <span class="o">=</span> <span class="n">qs</span> <span class="o">+</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span></span><a href="#l164"></a>
<span id="l165">        <span class="n">environ</span><span class="p">[</span><span class="s">&#39;QUERY_STRING&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">qs</span>    <span class="c"># XXX Shouldn&#39;t, really</span></span><a href="#l165"></a>
<span id="l166">    <span class="k">elif</span> <span class="s">&#39;QUERY_STRING&#39;</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span></span><a href="#l166"></a>
<span id="l167">        <span class="n">qs</span> <span class="o">=</span> <span class="n">environ</span><span class="p">[</span><span class="s">&#39;QUERY_STRING&#39;</span><span class="p">]</span></span><a href="#l167"></a>
<span id="l168">    <span class="k">else</span><span class="p">:</span></span><a href="#l168"></a>
<span id="l169">        <span class="k">if</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]:</span></span><a href="#l169"></a>
<span id="l170">            <span class="n">qs</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span></span><a href="#l170"></a>
<span id="l171">        <span class="k">else</span><span class="p">:</span></span><a href="#l171"></a>
<span id="l172">            <span class="n">qs</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l172"></a>
<span id="l173">        <span class="n">environ</span><span class="p">[</span><span class="s">&#39;QUERY_STRING&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">qs</span>    <span class="c"># XXX Shouldn&#39;t, really</span></span><a href="#l173"></a>
<span id="l174">    <span class="k">return</span> <span class="n">urlparse</span><span class="o">.</span><span class="n">parse_qs</span><span class="p">(</span><span class="n">qs</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="p">)</span></span><a href="#l174"></a>
<span id="l175"></span><a href="#l175"></a>
<span id="l176"></span><a href="#l176"></a>
<span id="l177"><span class="c"># parse query string function called from urlparse,</span></span><a href="#l177"></a>
<span id="l178"><span class="c"># this is done in order to maintain backward compatiblity.</span></span><a href="#l178"></a>
<span id="l179"></span><a href="#l179"></a>
<span id="l180"><span class="k">def</span> <span class="nf">parse_qs</span><span class="p">(</span><span class="n">qs</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></span><a href="#l180"></a>
<span id="l181">    <span class="sd">&quot;&quot;&quot;Parse a query given as a string argument.&quot;&quot;&quot;</span></span><a href="#l181"></a>
<span id="l182">    <span class="n">warn</span><span class="p">(</span><span class="s">&quot;cgi.parse_qs is deprecated, use urlparse.parse_qs instead&quot;</span><span class="p">,</span></span><a href="#l182"></a>
<span id="l183">         <span class="ne">PendingDeprecationWarning</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span></span><a href="#l183"></a>
<span id="l184">    <span class="k">return</span> <span class="n">urlparse</span><span class="o">.</span><span class="n">parse_qs</span><span class="p">(</span><span class="n">qs</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="p">)</span></span><a href="#l184"></a>
<span id="l185"></span><a href="#l185"></a>
<span id="l186"></span><a href="#l186"></a>
<span id="l187"><span class="k">def</span> <span class="nf">parse_qsl</span><span class="p">(</span><span class="n">qs</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></span><a href="#l187"></a>
<span id="l188">    <span class="sd">&quot;&quot;&quot;Parse a query given as a string argument.&quot;&quot;&quot;</span></span><a href="#l188"></a>
<span id="l189">    <span class="n">warn</span><span class="p">(</span><span class="s">&quot;cgi.parse_qsl is deprecated, use urlparse.parse_qsl instead&quot;</span><span class="p">,</span></span><a href="#l189"></a>
<span id="l190">         <span class="ne">PendingDeprecationWarning</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span></span><a href="#l190"></a>
<span id="l191">    <span class="k">return</span> <span class="n">urlparse</span><span class="o">.</span><span class="n">parse_qsl</span><span class="p">(</span><span class="n">qs</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="p">)</span></span><a href="#l191"></a>
<span id="l192"></span><a href="#l192"></a>
<span id="l193"><span class="k">def</span> <span class="nf">parse_multipart</span><span class="p">(</span><span class="n">fp</span><span class="p">,</span> <span class="n">pdict</span><span class="p">):</span></span><a href="#l193"></a>
<span id="l194">    <span class="sd">&quot;&quot;&quot;Parse multipart input.</span></span><a href="#l194"></a>
<span id="l195"></span><a href="#l195"></a>
<span id="l196"><span class="sd">    Arguments:</span></span><a href="#l196"></a>
<span id="l197"><span class="sd">    fp   : input file</span></span><a href="#l197"></a>
<span id="l198"><span class="sd">    pdict: dictionary containing other parameters of content-type header</span></span><a href="#l198"></a>
<span id="l199"></span><a href="#l199"></a>
<span id="l200"><span class="sd">    Returns a dictionary just like parse_qs(): keys are the field names, each</span></span><a href="#l200"></a>
<span id="l201"><span class="sd">    value is a list of values for that field.  This is easy to use but not</span></span><a href="#l201"></a>
<span id="l202"><span class="sd">    much good if you are expecting megabytes to be uploaded -- in that case,</span></span><a href="#l202"></a>
<span id="l203"><span class="sd">    use the FieldStorage class instead which is much more flexible.  Note</span></span><a href="#l203"></a>
<span id="l204"><span class="sd">    that content-type is the raw, unparsed contents of the content-type</span></span><a href="#l204"></a>
<span id="l205"><span class="sd">    header.</span></span><a href="#l205"></a>
<span id="l206"></span><a href="#l206"></a>
<span id="l207"><span class="sd">    XXX This does not parse nested multipart parts -- use FieldStorage for</span></span><a href="#l207"></a>
<span id="l208"><span class="sd">    that.</span></span><a href="#l208"></a>
<span id="l209"></span><a href="#l209"></a>
<span id="l210"><span class="sd">    XXX This should really be subsumed by FieldStorage altogether -- no</span></span><a href="#l210"></a>
<span id="l211"><span class="sd">    point in having two implementations of the same parsing algorithm.</span></span><a href="#l211"></a>
<span id="l212"><span class="sd">    Also, FieldStorage protects itself better against certain DoS attacks</span></span><a href="#l212"></a>
<span id="l213"><span class="sd">    by limiting the size of the data read in one chunk.  The API here</span></span><a href="#l213"></a>
<span id="l214"><span class="sd">    does not support that kind of protection.  This also affects parse()</span></span><a href="#l214"></a>
<span id="l215"><span class="sd">    since it can call parse_multipart().</span></span><a href="#l215"></a>
<span id="l216"></span><a href="#l216"></a>
<span id="l217"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l217"></a>
<span id="l218">    <span class="n">boundary</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l218"></a>
<span id="l219">    <span class="k">if</span> <span class="s">&#39;boundary&#39;</span> <span class="ow">in</span> <span class="n">pdict</span><span class="p">:</span></span><a href="#l219"></a>
<span id="l220">        <span class="n">boundary</span> <span class="o">=</span> <span class="n">pdict</span><span class="p">[</span><span class="s">&#39;boundary&#39;</span><span class="p">]</span></span><a href="#l220"></a>
<span id="l221">    <span class="k">if</span> <span class="ow">not</span> <span class="n">valid_boundary</span><span class="p">(</span><span class="n">boundary</span><span class="p">):</span></span><a href="#l221"></a>
<span id="l222">        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">,</span>  <span class="p">(</span><span class="s">&#39;Invalid boundary in multipart form: </span><span class="si">%r</span><span class="s">&#39;</span></span><a href="#l222"></a>
<span id="l223">                            <span class="o">%</span> <span class="p">(</span><span class="n">boundary</span><span class="p">,))</span></span><a href="#l223"></a>
<span id="l224"></span><a href="#l224"></a>
<span id="l225">    <span class="n">nextpart</span> <span class="o">=</span> <span class="s">&quot;--&quot;</span> <span class="o">+</span> <span class="n">boundary</span></span><a href="#l225"></a>
<span id="l226">    <span class="n">lastpart</span> <span class="o">=</span> <span class="s">&quot;--&quot;</span> <span class="o">+</span> <span class="n">boundary</span> <span class="o">+</span> <span class="s">&quot;--&quot;</span></span><a href="#l226"></a>
<span id="l227">    <span class="n">partdict</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l227"></a>
<span id="l228">    <span class="n">terminator</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l228"></a>
<span id="l229"></span><a href="#l229"></a>
<span id="l230">    <span class="k">while</span> <span class="n">terminator</span> <span class="o">!=</span> <span class="n">lastpart</span><span class="p">:</span></span><a href="#l230"></a>
<span id="l231">        <span class="nb">bytes</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l231"></a>
<span id="l232">        <span class="n">data</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l232"></a>
<span id="l233">        <span class="k">if</span> <span class="n">terminator</span><span class="p">:</span></span><a href="#l233"></a>
<span id="l234">            <span class="c"># At start of next part.  Read headers first.</span></span><a href="#l234"></a>
<span id="l235">            <span class="n">headers</span> <span class="o">=</span> <span class="n">mimetools</span><span class="o">.</span><span class="n">Message</span><span class="p">(</span><span class="n">fp</span><span class="p">)</span></span><a href="#l235"></a>
<span id="l236">            <span class="n">clength</span> <span class="o">=</span> <span class="n">headers</span><span class="o">.</span><span class="n">getheader</span><span class="p">(</span><span class="s">&#39;content-length&#39;</span><span class="p">)</span></span><a href="#l236"></a>
<span id="l237">            <span class="k">if</span> <span class="n">clength</span><span class="p">:</span></span><a href="#l237"></a>
<span id="l238">                <span class="k">try</span><span class="p">:</span></span><a href="#l238"></a>
<span id="l239">                    <span class="nb">bytes</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">clength</span><span class="p">)</span></span><a href="#l239"></a>
<span id="l240">                <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></span><a href="#l240"></a>
<span id="l241">                    <span class="k">pass</span></span><a href="#l241"></a>
<span id="l242">            <span class="k">if</span> <span class="nb">bytes</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l242"></a>
<span id="l243">                <span class="k">if</span> <span class="n">maxlen</span> <span class="ow">and</span> <span class="nb">bytes</span> <span class="o">&gt;</span> <span class="n">maxlen</span><span class="p">:</span></span><a href="#l243"></a>
<span id="l244">                    <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">,</span> <span class="s">&#39;Maximum content length exceeded&#39;</span></span><a href="#l244"></a>
<span id="l245">                <span class="n">data</span> <span class="o">=</span> <span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="nb">bytes</span><span class="p">)</span></span><a href="#l245"></a>
<span id="l246">            <span class="k">else</span><span class="p">:</span></span><a href="#l246"></a>
<span id="l247">                <span class="n">data</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l247"></a>
<span id="l248">        <span class="c"># Read lines until end of part.</span></span><a href="#l248"></a>
<span id="l249">        <span class="n">lines</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l249"></a>
<span id="l250">        <span class="k">while</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l250"></a>
<span id="l251">            <span class="n">line</span> <span class="o">=</span> <span class="n">fp</span><span class="o">.</span><span class="n">readline</span><span class="p">()</span></span><a href="#l251"></a>
<span id="l252">            <span class="k">if</span> <span class="ow">not</span> <span class="n">line</span><span class="p">:</span></span><a href="#l252"></a>
<span id="l253">                <span class="n">terminator</span> <span class="o">=</span> <span class="n">lastpart</span> <span class="c"># End outer loop</span></span><a href="#l253"></a>
<span id="l254">                <span class="k">break</span></span><a href="#l254"></a>
<span id="l255">            <span class="k">if</span> <span class="n">line</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;--&quot;</span><span class="p">:</span></span><a href="#l255"></a>
<span id="l256">                <span class="n">terminator</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l256"></a>
<span id="l257">                <span class="k">if</span> <span class="n">terminator</span> <span class="ow">in</span> <span class="p">(</span><span class="n">nextpart</span><span class="p">,</span> <span class="n">lastpart</span><span class="p">):</span></span><a href="#l257"></a>
<span id="l258">                    <span class="k">break</span></span><a href="#l258"></a>
<span id="l259">            <span class="n">lines</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></span><a href="#l259"></a>
<span id="l260">        <span class="c"># Done with part.</span></span><a href="#l260"></a>
<span id="l261">        <span class="k">if</span> <span class="n">data</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l261"></a>
<span id="l262">            <span class="k">continue</span></span><a href="#l262"></a>
<span id="l263">        <span class="k">if</span> <span class="nb">bytes</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l263"></a>
<span id="l264">            <span class="k">if</span> <span class="n">lines</span><span class="p">:</span></span><a href="#l264"></a>
<span id="l265">                <span class="c"># Strip final line terminator</span></span><a href="#l265"></a>
<span id="l266">                <span class="n">line</span> <span class="o">=</span> <span class="n">lines</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l266"></a>
<span id="l267">                <span class="k">if</span> <span class="n">line</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">:]</span> <span class="o">==</span> <span class="s">&quot;</span><span class="se">\r\n</span><span class="s">&quot;</span><span class="p">:</span></span><a href="#l267"></a>
<span id="l268">                    <span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="p">[:</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span></span><a href="#l268"></a>
<span id="l269">                <span class="k">elif</span> <span class="n">line</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">:]</span> <span class="o">==</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">:</span></span><a href="#l269"></a>
<span id="l270">                    <span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l270"></a>
<span id="l271">                <span class="n">lines</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">=</span> <span class="n">line</span></span><a href="#l271"></a>
<span id="l272">                <span class="n">data</span> <span class="o">=</span> <span class="s">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">lines</span><span class="p">)</span></span><a href="#l272"></a>
<span id="l273">        <span class="n">line</span> <span class="o">=</span> <span class="n">headers</span><span class="p">[</span><span class="s">&#39;content-disposition&#39;</span><span class="p">]</span></span><a href="#l273"></a>
<span id="l274">        <span class="k">if</span> <span class="ow">not</span> <span class="n">line</span><span class="p">:</span></span><a href="#l274"></a>
<span id="l275">            <span class="k">continue</span></span><a href="#l275"></a>
<span id="l276">        <span class="n">key</span><span class="p">,</span> <span class="n">params</span> <span class="o">=</span> <span class="n">parse_header</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></span><a href="#l276"></a>
<span id="l277">        <span class="k">if</span> <span class="n">key</span> <span class="o">!=</span> <span class="s">&#39;form-data&#39;</span><span class="p">:</span></span><a href="#l277"></a>
<span id="l278">            <span class="k">continue</span></span><a href="#l278"></a>
<span id="l279">        <span class="k">if</span> <span class="s">&#39;name&#39;</span> <span class="ow">in</span> <span class="n">params</span><span class="p">:</span></span><a href="#l279"></a>
<span id="l280">            <span class="n">name</span> <span class="o">=</span> <span class="n">params</span><span class="p">[</span><span class="s">&#39;name&#39;</span><span class="p">]</span></span><a href="#l280"></a>
<span id="l281">        <span class="k">else</span><span class="p">:</span></span><a href="#l281"></a>
<span id="l282">            <span class="k">continue</span></span><a href="#l282"></a>
<span id="l283">        <span class="k">if</span> <span class="n">name</span> <span class="ow">in</span> <span class="n">partdict</span><span class="p">:</span></span><a href="#l283"></a>
<span id="l284">            <span class="n">partdict</span><span class="p">[</span><span class="n">name</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></span><a href="#l284"></a>
<span id="l285">        <span class="k">else</span><span class="p">:</span></span><a href="#l285"></a>
<span id="l286">            <span class="n">partdict</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">data</span><span class="p">]</span></span><a href="#l286"></a>
<span id="l287"></span><a href="#l287"></a>
<span id="l288">    <span class="k">return</span> <span class="n">partdict</span></span><a href="#l288"></a>
<span id="l289"></span><a href="#l289"></a>
<span id="l290"></span><a href="#l290"></a>
<span id="l291"><span class="k">def</span> <span class="nf">_parseparam</span><span class="p">(</span><span class="n">s</span><span class="p">):</span></span><a href="#l291"></a>
<span id="l292">    <span class="k">while</span> <span class="n">s</span><span class="p">[:</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;;&#39;</span><span class="p">:</span></span><a href="#l292"></a>
<span id="l293">        <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="p">[</span><span class="mi">1</span><span class="p">:]</span></span><a href="#l293"></a>
<span id="l294">        <span class="n">end</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s">&#39;;&#39;</span><span class="p">)</span></span><a href="#l294"></a>
<span id="l295">        <span class="k">while</span> <span class="n">end</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="p">(</span><span class="n">s</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;&quot;&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">end</span><span class="p">)</span> <span class="o">-</span> <span class="n">s</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\\</span><span class="s">&quot;&#39;</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="n">end</span><span class="p">))</span> <span class="o">%</span> <span class="mi">2</span><span class="p">:</span></span><a href="#l295"></a>
<span id="l296">            <span class="n">end</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s">&#39;;&#39;</span><span class="p">,</span> <span class="n">end</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span></span><a href="#l296"></a>
<span id="l297">        <span class="k">if</span> <span class="n">end</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l297"></a>
<span id="l298">            <span class="n">end</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">s</span><span class="p">)</span></span><a href="#l298"></a>
<span id="l299">        <span class="n">f</span> <span class="o">=</span> <span class="n">s</span><span class="p">[:</span><span class="n">end</span><span class="p">]</span></span><a href="#l299"></a>
<span id="l300">        <span class="k">yield</span> <span class="n">f</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l300"></a>
<span id="l301">        <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="p">[</span><span class="n">end</span><span class="p">:]</span></span><a href="#l301"></a>
<span id="l302"></span><a href="#l302"></a>
<span id="l303"><span class="k">def</span> <span class="nf">parse_header</span><span class="p">(</span><span class="n">line</span><span class="p">):</span></span><a href="#l303"></a>
<span id="l304">    <span class="sd">&quot;&quot;&quot;Parse a Content-type like header.</span></span><a href="#l304"></a>
<span id="l305"></span><a href="#l305"></a>
<span id="l306"><span class="sd">    Return the main content-type and a dictionary of options.</span></span><a href="#l306"></a>
<span id="l307"></span><a href="#l307"></a>
<span id="l308"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l308"></a>
<span id="l309">    <span class="n">parts</span> <span class="o">=</span> <span class="n">_parseparam</span><span class="p">(</span><span class="s">&#39;;&#39;</span> <span class="o">+</span> <span class="n">line</span><span class="p">)</span></span><a href="#l309"></a>
<span id="l310">    <span class="n">key</span> <span class="o">=</span> <span class="n">parts</span><span class="o">.</span><span class="n">next</span><span class="p">()</span></span><a href="#l310"></a>
<span id="l311">    <span class="n">pdict</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l311"></a>
<span id="l312">    <span class="k">for</span> <span class="n">p</span> <span class="ow">in</span> <span class="n">parts</span><span class="p">:</span></span><a href="#l312"></a>
<span id="l313">        <span class="n">i</span> <span class="o">=</span> <span class="n">p</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s">&#39;=&#39;</span><span class="p">)</span></span><a href="#l313"></a>
<span id="l314">        <span class="k">if</span> <span class="n">i</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l314"></a>
<span id="l315">            <span class="n">name</span> <span class="o">=</span> <span class="n">p</span><span class="p">[:</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span><span class="o">.</span><span class="n">lower</span><span class="p">()</span></span><a href="#l315"></a>
<span id="l316">            <span class="n">value</span> <span class="o">=</span> <span class="n">p</span><span class="p">[</span><span class="n">i</span><span class="o">+</span><span class="mi">1</span><span class="p">:]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l316"></a>
<span id="l317">            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">value</span><span class="p">)</span> <span class="o">&gt;=</span> <span class="mi">2</span> <span class="ow">and</span> <span class="n">value</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="n">value</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;&quot;&#39;</span><span class="p">:</span></span><a href="#l317"></a>
<span id="l318">                <span class="n">value</span> <span class="o">=</span> <span class="n">value</span><span class="p">[</span><span class="mi">1</span><span class="p">:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l318"></a>
<span id="l319">                <span class="n">value</span> <span class="o">=</span> <span class="n">value</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\\\\</span><span class="s">&#39;</span><span class="p">,</span> <span class="s">&#39;</span><span class="se">\\</span><span class="s">&#39;</span><span class="p">)</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\\</span><span class="s">&quot;&#39;</span><span class="p">,</span> <span class="s">&#39;&quot;&#39;</span><span class="p">)</span></span><a href="#l319"></a>
<span id="l320">            <span class="n">pdict</span><span class="p">[</span><span class="n">name</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span></span><a href="#l320"></a>
<span id="l321">    <span class="k">return</span> <span class="n">key</span><span class="p">,</span> <span class="n">pdict</span></span><a href="#l321"></a>
<span id="l322"></span><a href="#l322"></a>
<span id="l323"></span><a href="#l323"></a>
<span id="l324"><span class="c"># Classes for field storage</span></span><a href="#l324"></a>
<span id="l325"><span class="c"># =========================</span></span><a href="#l325"></a>
<span id="l326"></span><a href="#l326"></a>
<span id="l327"><span class="k">class</span> <span class="nc">MiniFieldStorage</span><span class="p">:</span></span><a href="#l327"></a>
<span id="l328"></span><a href="#l328"></a>
<span id="l329">    <span class="sd">&quot;&quot;&quot;Like FieldStorage, for use when no file uploads are possible.&quot;&quot;&quot;</span></span><a href="#l329"></a>
<span id="l330"></span><a href="#l330"></a>
<span id="l331">    <span class="c"># Dummy attributes</span></span><a href="#l331"></a>
<span id="l332">    <span class="n">filename</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l332"></a>
<span id="l333">    <span class="nb">list</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l333"></a>
<span id="l334">    <span class="nb">type</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l334"></a>
<span id="l335">    <span class="nb">file</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l335"></a>
<span id="l336">    <span class="n">type_options</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l336"></a>
<span id="l337">    <span class="n">disposition</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l337"></a>
<span id="l338">    <span class="n">disposition_options</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l338"></a>
<span id="l339">    <span class="n">headers</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l339"></a>
<span id="l340"></span><a href="#l340"></a>
<span id="l341">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span></span><a href="#l341"></a>
<span id="l342">        <span class="sd">&quot;&quot;&quot;Constructor from field name and value.&quot;&quot;&quot;</span></span><a href="#l342"></a>
<span id="l343">        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">name</span></span><a href="#l343"></a>
<span id="l344">        <span class="bp">self</span><span class="o">.</span><span class="n">value</span> <span class="o">=</span> <span class="n">value</span></span><a href="#l344"></a>
<span id="l345">        <span class="c"># self.file = StringIO(value)</span></span><a href="#l345"></a>
<span id="l346"></span><a href="#l346"></a>
<span id="l347">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l347"></a>
<span id="l348">        <span class="sd">&quot;&quot;&quot;Return printable representation.&quot;&quot;&quot;</span></span><a href="#l348"></a>
<span id="l349">        <span class="k">return</span> <span class="s">&quot;MiniFieldStorage(</span><span class="si">%r</span><span class="s">, </span><span class="si">%r</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></span><a href="#l349"></a>
<span id="l350"></span><a href="#l350"></a>
<span id="l351"></span><a href="#l351"></a>
<span id="l352"><span class="k">class</span> <span class="nc">FieldStorage</span><span class="p">:</span></span><a href="#l352"></a>
<span id="l353"></span><a href="#l353"></a>
<span id="l354">    <span class="sd">&quot;&quot;&quot;Store a sequence of fields, reading multipart/form-data.</span></span><a href="#l354"></a>
<span id="l355"></span><a href="#l355"></a>
<span id="l356"><span class="sd">    This class provides naming, typing, files stored on disk, and</span></span><a href="#l356"></a>
<span id="l357"><span class="sd">    more.  At the top level, it is accessible like a dictionary, whose</span></span><a href="#l357"></a>
<span id="l358"><span class="sd">    keys are the field names.  (Note: None can occur as a field name.)</span></span><a href="#l358"></a>
<span id="l359"><span class="sd">    The items are either a Python list (if there&#39;s multiple values) or</span></span><a href="#l359"></a>
<span id="l360"><span class="sd">    another FieldStorage or MiniFieldStorage object.  If it&#39;s a single</span></span><a href="#l360"></a>
<span id="l361"><span class="sd">    object, it has the following attributes:</span></span><a href="#l361"></a>
<span id="l362"></span><a href="#l362"></a>
<span id="l363"><span class="sd">    name: the field name, if specified; otherwise None</span></span><a href="#l363"></a>
<span id="l364"></span><a href="#l364"></a>
<span id="l365"><span class="sd">    filename: the filename, if specified; otherwise None; this is the</span></span><a href="#l365"></a>
<span id="l366"><span class="sd">        client side filename, *not* the file name on which it is</span></span><a href="#l366"></a>
<span id="l367"><span class="sd">        stored (that&#39;s a temporary file you don&#39;t deal with)</span></span><a href="#l367"></a>
<span id="l368"></span><a href="#l368"></a>
<span id="l369"><span class="sd">    value: the value as a *string*; for file uploads, this</span></span><a href="#l369"></a>
<span id="l370"><span class="sd">        transparently reads the file every time you request the value</span></span><a href="#l370"></a>
<span id="l371"></span><a href="#l371"></a>
<span id="l372"><span class="sd">    file: the file(-like) object from which you can read the data;</span></span><a href="#l372"></a>
<span id="l373"><span class="sd">        None if the data is stored a simple string</span></span><a href="#l373"></a>
<span id="l374"></span><a href="#l374"></a>
<span id="l375"><span class="sd">    type: the content-type, or None if not specified</span></span><a href="#l375"></a>
<span id="l376"></span><a href="#l376"></a>
<span id="l377"><span class="sd">    type_options: dictionary of options specified on the content-type</span></span><a href="#l377"></a>
<span id="l378"><span class="sd">        line</span></span><a href="#l378"></a>
<span id="l379"></span><a href="#l379"></a>
<span id="l380"><span class="sd">    disposition: content-disposition, or None if not specified</span></span><a href="#l380"></a>
<span id="l381"></span><a href="#l381"></a>
<span id="l382"><span class="sd">    disposition_options: dictionary of corresponding options</span></span><a href="#l382"></a>
<span id="l383"></span><a href="#l383"></a>
<span id="l384"><span class="sd">    headers: a dictionary(-like) object (sometimes rfc822.Message or a</span></span><a href="#l384"></a>
<span id="l385"><span class="sd">        subclass thereof) containing *all* headers</span></span><a href="#l385"></a>
<span id="l386"></span><a href="#l386"></a>
<span id="l387"><span class="sd">    The class is subclassable, mostly for the purpose of overriding</span></span><a href="#l387"></a>
<span id="l388"><span class="sd">    the make_file() method, which is called internally to come up with</span></span><a href="#l388"></a>
<span id="l389"><span class="sd">    a file open for reading and writing.  This makes it possible to</span></span><a href="#l389"></a>
<span id="l390"><span class="sd">    override the default choice of storing all files in a temporary</span></span><a href="#l390"></a>
<span id="l391"><span class="sd">    directory and unlinking them as soon as they have been opened.</span></span><a href="#l391"></a>
<span id="l392"></span><a href="#l392"></a>
<span id="l393"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l393"></a>
<span id="l394"></span><a href="#l394"></a>
<span id="l395">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">fp</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">outerboundary</span><span class="o">=</span><span class="s">&quot;&quot;</span><span class="p">,</span></span><a href="#l395"></a>
<span id="l396">                 <span class="n">environ</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></span><a href="#l396"></a>
<span id="l397">        <span class="sd">&quot;&quot;&quot;Constructor.  Read multipart/* until last part.</span></span><a href="#l397"></a>
<span id="l398"></span><a href="#l398"></a>
<span id="l399"><span class="sd">        Arguments, all optional:</span></span><a href="#l399"></a>
<span id="l400"></span><a href="#l400"></a>
<span id="l401"><span class="sd">        fp              : file pointer; default: sys.stdin</span></span><a href="#l401"></a>
<span id="l402"><span class="sd">            (not used when the request method is GET)</span></span><a href="#l402"></a>
<span id="l403"></span><a href="#l403"></a>
<span id="l404"><span class="sd">        headers         : header dictionary-like object; default:</span></span><a href="#l404"></a>
<span id="l405"><span class="sd">            taken from environ as per CGI spec</span></span><a href="#l405"></a>
<span id="l406"></span><a href="#l406"></a>
<span id="l407"><span class="sd">        outerboundary   : terminating multipart boundary</span></span><a href="#l407"></a>
<span id="l408"><span class="sd">            (for internal use only)</span></span><a href="#l408"></a>
<span id="l409"></span><a href="#l409"></a>
<span id="l410"><span class="sd">        environ         : environment dictionary; default: os.environ</span></span><a href="#l410"></a>
<span id="l411"></span><a href="#l411"></a>
<span id="l412"><span class="sd">        keep_blank_values: flag indicating whether blank values in</span></span><a href="#l412"></a>
<span id="l413"><span class="sd">            percent-encoded forms should be treated as blank strings.</span></span><a href="#l413"></a>
<span id="l414"><span class="sd">            A true value indicates that blanks should be retained as</span></span><a href="#l414"></a>
<span id="l415"><span class="sd">            blank strings.  The default false value indicates that</span></span><a href="#l415"></a>
<span id="l416"><span class="sd">            blank values are to be ignored and treated as if they were</span></span><a href="#l416"></a>
<span id="l417"><span class="sd">            not included.</span></span><a href="#l417"></a>
<span id="l418"></span><a href="#l418"></a>
<span id="l419"><span class="sd">        strict_parsing: flag indicating what to do with parsing errors.</span></span><a href="#l419"></a>
<span id="l420"><span class="sd">            If false (the default), errors are silently ignored.</span></span><a href="#l420"></a>
<span id="l421"><span class="sd">            If true, errors raise a ValueError exception.</span></span><a href="#l421"></a>
<span id="l422"></span><a href="#l422"></a>
<span id="l423"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l423"></a>
<span id="l424">        <span class="n">method</span> <span class="o">=</span> <span class="s">&#39;GET&#39;</span></span><a href="#l424"></a>
<span id="l425">        <span class="bp">self</span><span class="o">.</span><span class="n">keep_blank_values</span> <span class="o">=</span> <span class="n">keep_blank_values</span></span><a href="#l425"></a>
<span id="l426">        <span class="bp">self</span><span class="o">.</span><span class="n">strict_parsing</span> <span class="o">=</span> <span class="n">strict_parsing</span></span><a href="#l426"></a>
<span id="l427">        <span class="k">if</span> <span class="s">&#39;REQUEST_METHOD&#39;</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span></span><a href="#l427"></a>
<span id="l428">            <span class="n">method</span> <span class="o">=</span> <span class="n">environ</span><span class="p">[</span><span class="s">&#39;REQUEST_METHOD&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">upper</span><span class="p">()</span></span><a href="#l428"></a>
<span id="l429">        <span class="bp">self</span><span class="o">.</span><span class="n">qs_on_post</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l429"></a>
<span id="l430">        <span class="k">if</span> <span class="n">method</span> <span class="o">==</span> <span class="s">&#39;GET&#39;</span> <span class="ow">or</span> <span class="n">method</span> <span class="o">==</span> <span class="s">&#39;HEAD&#39;</span><span class="p">:</span></span><a href="#l430"></a>
<span id="l431">            <span class="k">if</span> <span class="s">&#39;QUERY_STRING&#39;</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span></span><a href="#l431"></a>
<span id="l432">                <span class="n">qs</span> <span class="o">=</span> <span class="n">environ</span><span class="p">[</span><span class="s">&#39;QUERY_STRING&#39;</span><span class="p">]</span></span><a href="#l432"></a>
<span id="l433">            <span class="k">elif</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">:]:</span></span><a href="#l433"></a>
<span id="l434">                <span class="n">qs</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span></span><a href="#l434"></a>
<span id="l435">            <span class="k">else</span><span class="p">:</span></span><a href="#l435"></a>
<span id="l436">                <span class="n">qs</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l436"></a>
<span id="l437">            <span class="n">fp</span> <span class="o">=</span> <span class="n">StringIO</span><span class="p">(</span><span class="n">qs</span><span class="p">)</span></span><a href="#l437"></a>
<span id="l438">            <span class="k">if</span> <span class="n">headers</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l438"></a>
<span id="l439">                <span class="n">headers</span> <span class="o">=</span> <span class="p">{</span><span class="s">&#39;content-type&#39;</span><span class="p">:</span></span><a href="#l439"></a>
<span id="l440">                           <span class="s">&quot;application/x-www-form-urlencoded&quot;</span><span class="p">}</span></span><a href="#l440"></a>
<span id="l441">        <span class="k">if</span> <span class="n">headers</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l441"></a>
<span id="l442">            <span class="n">headers</span> <span class="o">=</span> <span class="p">{}</span></span><a href="#l442"></a>
<span id="l443">            <span class="k">if</span> <span class="n">method</span> <span class="o">==</span> <span class="s">&#39;POST&#39;</span><span class="p">:</span></span><a href="#l443"></a>
<span id="l444">                <span class="c"># Set default content-type for POST to what&#39;s traditional</span></span><a href="#l444"></a>
<span id="l445">                <span class="n">headers</span><span class="p">[</span><span class="s">&#39;content-type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="s">&quot;application/x-www-form-urlencoded&quot;</span></span><a href="#l445"></a>
<span id="l446">            <span class="k">if</span> <span class="s">&#39;CONTENT_TYPE&#39;</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span></span><a href="#l446"></a>
<span id="l447">                <span class="n">headers</span><span class="p">[</span><span class="s">&#39;content-type&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">environ</span><span class="p">[</span><span class="s">&#39;CONTENT_TYPE&#39;</span><span class="p">]</span></span><a href="#l447"></a>
<span id="l448">            <span class="k">if</span> <span class="s">&#39;QUERY_STRING&#39;</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span></span><a href="#l448"></a>
<span id="l449">                <span class="bp">self</span><span class="o">.</span><span class="n">qs_on_post</span> <span class="o">=</span> <span class="n">environ</span><span class="p">[</span><span class="s">&#39;QUERY_STRING&#39;</span><span class="p">]</span></span><a href="#l449"></a>
<span id="l450">            <span class="k">if</span> <span class="s">&#39;CONTENT_LENGTH&#39;</span> <span class="ow">in</span> <span class="n">environ</span><span class="p">:</span></span><a href="#l450"></a>
<span id="l451">                <span class="n">headers</span><span class="p">[</span><span class="s">&#39;content-length&#39;</span><span class="p">]</span> <span class="o">=</span> <span class="n">environ</span><span class="p">[</span><span class="s">&#39;CONTENT_LENGTH&#39;</span><span class="p">]</span></span><a href="#l451"></a>
<span id="l452">        <span class="bp">self</span><span class="o">.</span><span class="n">fp</span> <span class="o">=</span> <span class="n">fp</span> <span class="ow">or</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdin</span></span><a href="#l452"></a>
<span id="l453">        <span class="bp">self</span><span class="o">.</span><span class="n">headers</span> <span class="o">=</span> <span class="n">headers</span></span><a href="#l453"></a>
<span id="l454">        <span class="bp">self</span><span class="o">.</span><span class="n">outerboundary</span> <span class="o">=</span> <span class="n">outerboundary</span></span><a href="#l454"></a>
<span id="l455"></span><a href="#l455"></a>
<span id="l456">        <span class="c"># Process content-disposition header</span></span><a href="#l456"></a>
<span id="l457">        <span class="n">cdisp</span><span class="p">,</span> <span class="n">pdict</span> <span class="o">=</span> <span class="s">&quot;&quot;</span><span class="p">,</span> <span class="p">{}</span></span><a href="#l457"></a>
<span id="l458">        <span class="k">if</span> <span class="s">&#39;content-disposition&#39;</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">:</span></span><a href="#l458"></a>
<span id="l459">            <span class="n">cdisp</span><span class="p">,</span> <span class="n">pdict</span> <span class="o">=</span> <span class="n">parse_header</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">[</span><span class="s">&#39;content-disposition&#39;</span><span class="p">])</span></span><a href="#l459"></a>
<span id="l460">        <span class="bp">self</span><span class="o">.</span><span class="n">disposition</span> <span class="o">=</span> <span class="n">cdisp</span></span><a href="#l460"></a>
<span id="l461">        <span class="bp">self</span><span class="o">.</span><span class="n">disposition_options</span> <span class="o">=</span> <span class="n">pdict</span></span><a href="#l461"></a>
<span id="l462">        <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l462"></a>
<span id="l463">        <span class="k">if</span> <span class="s">&#39;name&#39;</span> <span class="ow">in</span> <span class="n">pdict</span><span class="p">:</span></span><a href="#l463"></a>
<span id="l464">            <span class="bp">self</span><span class="o">.</span><span class="n">name</span> <span class="o">=</span> <span class="n">pdict</span><span class="p">[</span><span class="s">&#39;name&#39;</span><span class="p">]</span></span><a href="#l464"></a>
<span id="l465">        <span class="bp">self</span><span class="o">.</span><span class="n">filename</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l465"></a>
<span id="l466">        <span class="k">if</span> <span class="s">&#39;filename&#39;</span> <span class="ow">in</span> <span class="n">pdict</span><span class="p">:</span></span><a href="#l466"></a>
<span id="l467">            <span class="bp">self</span><span class="o">.</span><span class="n">filename</span> <span class="o">=</span> <span class="n">pdict</span><span class="p">[</span><span class="s">&#39;filename&#39;</span><span class="p">]</span></span><a href="#l467"></a>
<span id="l468"></span><a href="#l468"></a>
<span id="l469">        <span class="c"># Process content-type header</span></span><a href="#l469"></a>
<span id="l470">        <span class="c">#</span></span><a href="#l470"></a>
<span id="l471">        <span class="c"># Honor any existing content-type header.  But if there is no</span></span><a href="#l471"></a>
<span id="l472">        <span class="c"># content-type header, use some sensible defaults.  Assume</span></span><a href="#l472"></a>
<span id="l473">        <span class="c"># outerboundary is &quot;&quot; at the outer level, but something non-false</span></span><a href="#l473"></a>
<span id="l474">        <span class="c"># inside a multi-part.  The default for an inner part is text/plain,</span></span><a href="#l474"></a>
<span id="l475">        <span class="c"># but for an outer part it should be urlencoded.  This should catch</span></span><a href="#l475"></a>
<span id="l476">        <span class="c"># bogus clients which erroneously forget to include a content-type</span></span><a href="#l476"></a>
<span id="l477">        <span class="c"># header.</span></span><a href="#l477"></a>
<span id="l478">        <span class="c">#</span></span><a href="#l478"></a>
<span id="l479">        <span class="c"># See below for what we do if there does exist a content-type header,</span></span><a href="#l479"></a>
<span id="l480">        <span class="c"># but it happens to be something we don&#39;t understand.</span></span><a href="#l480"></a>
<span id="l481">        <span class="k">if</span> <span class="s">&#39;content-type&#39;</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">:</span></span><a href="#l481"></a>
<span id="l482">            <span class="n">ctype</span><span class="p">,</span> <span class="n">pdict</span> <span class="o">=</span> <span class="n">parse_header</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">[</span><span class="s">&#39;content-type&#39;</span><span class="p">])</span></span><a href="#l482"></a>
<span id="l483">        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">outerboundary</span> <span class="ow">or</span> <span class="n">method</span> <span class="o">!=</span> <span class="s">&#39;POST&#39;</span><span class="p">:</span></span><a href="#l483"></a>
<span id="l484">            <span class="n">ctype</span><span class="p">,</span> <span class="n">pdict</span> <span class="o">=</span> <span class="s">&quot;text/plain&quot;</span><span class="p">,</span> <span class="p">{}</span></span><a href="#l484"></a>
<span id="l485">        <span class="k">else</span><span class="p">:</span></span><a href="#l485"></a>
<span id="l486">            <span class="n">ctype</span><span class="p">,</span> <span class="n">pdict</span> <span class="o">=</span> <span class="s">&#39;application/x-www-form-urlencoded&#39;</span><span class="p">,</span> <span class="p">{}</span></span><a href="#l486"></a>
<span id="l487">        <span class="bp">self</span><span class="o">.</span><span class="n">type</span> <span class="o">=</span> <span class="n">ctype</span></span><a href="#l487"></a>
<span id="l488">        <span class="bp">self</span><span class="o">.</span><span class="n">type_options</span> <span class="o">=</span> <span class="n">pdict</span></span><a href="#l488"></a>
<span id="l489">        <span class="bp">self</span><span class="o">.</span><span class="n">innerboundary</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l489"></a>
<span id="l490">        <span class="k">if</span> <span class="s">&#39;boundary&#39;</span> <span class="ow">in</span> <span class="n">pdict</span><span class="p">:</span></span><a href="#l490"></a>
<span id="l491">            <span class="bp">self</span><span class="o">.</span><span class="n">innerboundary</span> <span class="o">=</span> <span class="n">pdict</span><span class="p">[</span><span class="s">&#39;boundary&#39;</span><span class="p">]</span></span><a href="#l491"></a>
<span id="l492">        <span class="n">clen</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l492"></a>
<span id="l493">        <span class="k">if</span> <span class="s">&#39;content-length&#39;</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">:</span></span><a href="#l493"></a>
<span id="l494">            <span class="k">try</span><span class="p">:</span></span><a href="#l494"></a>
<span id="l495">                <span class="n">clen</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">headers</span><span class="p">[</span><span class="s">&#39;content-length&#39;</span><span class="p">])</span></span><a href="#l495"></a>
<span id="l496">            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></span><a href="#l496"></a>
<span id="l497">                <span class="k">pass</span></span><a href="#l497"></a>
<span id="l498">            <span class="k">if</span> <span class="n">maxlen</span> <span class="ow">and</span> <span class="n">clen</span> <span class="o">&gt;</span> <span class="n">maxlen</span><span class="p">:</span></span><a href="#l498"></a>
<span id="l499">                <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">,</span> <span class="s">&#39;Maximum content length exceeded&#39;</span></span><a href="#l499"></a>
<span id="l500">        <span class="bp">self</span><span class="o">.</span><span class="n">length</span> <span class="o">=</span> <span class="n">clen</span></span><a href="#l500"></a>
<span id="l501"></span><a href="#l501"></a>
<span id="l502">        <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l502"></a>
<span id="l503">        <span class="bp">self</span><span class="o">.</span><span class="n">done</span> <span class="o">=</span> <span class="mi">0</span></span><a href="#l503"></a>
<span id="l504">        <span class="k">if</span> <span class="n">ctype</span> <span class="o">==</span> <span class="s">&#39;application/x-www-form-urlencoded&#39;</span><span class="p">:</span></span><a href="#l504"></a>
<span id="l505">            <span class="bp">self</span><span class="o">.</span><span class="n">read_urlencoded</span><span class="p">()</span></span><a href="#l505"></a>
<span id="l506">        <span class="k">elif</span> <span class="n">ctype</span><span class="p">[:</span><span class="mi">10</span><span class="p">]</span> <span class="o">==</span> <span class="s">&#39;multipart/&#39;</span><span class="p">:</span></span><a href="#l506"></a>
<span id="l507">            <span class="bp">self</span><span class="o">.</span><span class="n">read_multi</span><span class="p">(</span><span class="n">environ</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="p">)</span></span><a href="#l507"></a>
<span id="l508">        <span class="k">else</span><span class="p">:</span></span><a href="#l508"></a>
<span id="l509">            <span class="bp">self</span><span class="o">.</span><span class="n">read_single</span><span class="p">()</span></span><a href="#l509"></a>
<span id="l510"></span><a href="#l510"></a>
<span id="l511">    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l511"></a>
<span id="l512">        <span class="sd">&quot;&quot;&quot;Return a printable representation.&quot;&quot;&quot;</span></span><a href="#l512"></a>
<span id="l513">        <span class="k">return</span> <span class="s">&quot;FieldStorage(</span><span class="si">%r</span><span class="s">, </span><span class="si">%r</span><span class="s">, </span><span class="si">%r</span><span class="s">)&quot;</span> <span class="o">%</span> <span class="p">(</span></span><a href="#l513"></a>
<span id="l514">                <span class="bp">self</span><span class="o">.</span><span class="n">name</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">filename</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">value</span><span class="p">)</span></span><a href="#l514"></a>
<span id="l515"></span><a href="#l515"></a>
<span id="l516">    <span class="k">def</span> <span class="nf">__iter__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l516"></a>
<span id="l517">        <span class="k">return</span> <span class="nb">iter</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span></span><a href="#l517"></a>
<span id="l518"></span><a href="#l518"></a>
<span id="l519">    <span class="k">def</span> <span class="nf">__getattr__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">name</span><span class="p">):</span></span><a href="#l519"></a>
<span id="l520">        <span class="k">if</span> <span class="n">name</span> <span class="o">!=</span> <span class="s">&#39;value&#39;</span><span class="p">:</span></span><a href="#l520"></a>
<span id="l521">            <span class="k">raise</span> <span class="ne">AttributeError</span><span class="p">,</span> <span class="n">name</span></span><a href="#l521"></a>
<span id="l522">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="p">:</span></span><a href="#l522"></a>
<span id="l523">            <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></span><a href="#l523"></a>
<span id="l524">            <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">read</span><span class="p">()</span></span><a href="#l524"></a>
<span id="l525">            <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></span><a href="#l525"></a>
<span id="l526">        <span class="k">elif</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l526"></a>
<span id="l527">            <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span></span><a href="#l527"></a>
<span id="l528">        <span class="k">else</span><span class="p">:</span></span><a href="#l528"></a>
<span id="l529">            <span class="n">value</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l529"></a>
<span id="l530">        <span class="k">return</span> <span class="n">value</span></span><a href="#l530"></a>
<span id="l531"></span><a href="#l531"></a>
<span id="l532">    <span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l532"></a>
<span id="l533">        <span class="sd">&quot;&quot;&quot;Dictionary style indexing.&quot;&quot;&quot;</span></span><a href="#l533"></a>
<span id="l534">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l534"></a>
<span id="l535">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">,</span> <span class="s">&quot;not indexable&quot;</span></span><a href="#l535"></a>
<span id="l536">        <span class="n">found</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l536"></a>
<span id="l537">        <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="p">:</span></span><a href="#l537"></a>
<span id="l538">            <span class="k">if</span> <span class="n">item</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="n">key</span><span class="p">:</span> <span class="n">found</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">item</span><span class="p">)</span></span><a href="#l538"></a>
<span id="l539">        <span class="k">if</span> <span class="ow">not</span> <span class="n">found</span><span class="p">:</span></span><a href="#l539"></a>
<span id="l540">            <span class="k">raise</span> <span class="ne">KeyError</span><span class="p">,</span> <span class="n">key</span></span><a href="#l540"></a>
<span id="l541">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">found</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l541"></a>
<span id="l542">            <span class="k">return</span> <span class="n">found</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span></span><a href="#l542"></a>
<span id="l543">        <span class="k">else</span><span class="p">:</span></span><a href="#l543"></a>
<span id="l544">            <span class="k">return</span> <span class="n">found</span></span><a href="#l544"></a>
<span id="l545"></span><a href="#l545"></a>
<span id="l546">    <span class="k">def</span> <span class="nf">getvalue</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l546"></a>
<span id="l547">        <span class="sd">&quot;&quot;&quot;Dictionary style get() method, including &#39;value&#39; lookup.&quot;&quot;&quot;</span></span><a href="#l547"></a>
<span id="l548">        <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span></span><a href="#l548"></a>
<span id="l549">            <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span></span><a href="#l549"></a>
<span id="l550">            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">)</span> <span class="ow">is</span> <span class="nb">type</span><span class="p">([]):</span></span><a href="#l550"></a>
<span id="l551">                <span class="k">return</span> <span class="nb">map</span><span class="p">(</span><span class="n">attrgetter</span><span class="p">(</span><span class="s">&#39;value&#39;</span><span class="p">),</span> <span class="n">value</span><span class="p">)</span></span><a href="#l551"></a>
<span id="l552">            <span class="k">else</span><span class="p">:</span></span><a href="#l552"></a>
<span id="l553">                <span class="k">return</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span></span><a href="#l553"></a>
<span id="l554">        <span class="k">else</span><span class="p">:</span></span><a href="#l554"></a>
<span id="l555">            <span class="k">return</span> <span class="n">default</span></span><a href="#l555"></a>
<span id="l556"></span><a href="#l556"></a>
<span id="l557">    <span class="k">def</span> <span class="nf">getfirst</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">default</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l557"></a>
<span id="l558">        <span class="sd">&quot;&quot;&quot; Return the first value received.&quot;&quot;&quot;</span></span><a href="#l558"></a>
<span id="l559">        <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span></span><a href="#l559"></a>
<span id="l560">            <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span></span><a href="#l560"></a>
<span id="l561">            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">)</span> <span class="ow">is</span> <span class="nb">type</span><span class="p">([]):</span></span><a href="#l561"></a>
<span id="l562">                <span class="k">return</span> <span class="n">value</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">value</span></span><a href="#l562"></a>
<span id="l563">            <span class="k">else</span><span class="p">:</span></span><a href="#l563"></a>
<span id="l564">                <span class="k">return</span> <span class="n">value</span><span class="o">.</span><span class="n">value</span></span><a href="#l564"></a>
<span id="l565">        <span class="k">else</span><span class="p">:</span></span><a href="#l565"></a>
<span id="l566">            <span class="k">return</span> <span class="n">default</span></span><a href="#l566"></a>
<span id="l567"></span><a href="#l567"></a>
<span id="l568">    <span class="k">def</span> <span class="nf">getlist</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l568"></a>
<span id="l569">        <span class="sd">&quot;&quot;&quot; Return list of received values.&quot;&quot;&quot;</span></span><a href="#l569"></a>
<span id="l570">        <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="p">:</span></span><a href="#l570"></a>
<span id="l571">            <span class="n">value</span> <span class="o">=</span> <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]</span></span><a href="#l571"></a>
<span id="l572">            <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">)</span> <span class="ow">is</span> <span class="nb">type</span><span class="p">([]):</span></span><a href="#l572"></a>
<span id="l573">                <span class="k">return</span> <span class="nb">map</span><span class="p">(</span><span class="n">attrgetter</span><span class="p">(</span><span class="s">&#39;value&#39;</span><span class="p">),</span> <span class="n">value</span><span class="p">)</span></span><a href="#l573"></a>
<span id="l574">            <span class="k">else</span><span class="p">:</span></span><a href="#l574"></a>
<span id="l575">                <span class="k">return</span> <span class="p">[</span><span class="n">value</span><span class="o">.</span><span class="n">value</span><span class="p">]</span></span><a href="#l575"></a>
<span id="l576">        <span class="k">else</span><span class="p">:</span></span><a href="#l576"></a>
<span id="l577">            <span class="k">return</span> <span class="p">[]</span></span><a href="#l577"></a>
<span id="l578"></span><a href="#l578"></a>
<span id="l579">    <span class="k">def</span> <span class="nf">keys</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l579"></a>
<span id="l580">        <span class="sd">&quot;&quot;&quot;Dictionary style keys() method.&quot;&quot;&quot;</span></span><a href="#l580"></a>
<span id="l581">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l581"></a>
<span id="l582">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">,</span> <span class="s">&quot;not indexable&quot;</span></span><a href="#l582"></a>
<span id="l583">        <span class="k">return</span> <span class="nb">list</span><span class="p">(</span><span class="nb">set</span><span class="p">(</span><span class="n">item</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="p">))</span></span><a href="#l583"></a>
<span id="l584"></span><a href="#l584"></a>
<span id="l585">    <span class="k">def</span> <span class="nf">has_key</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l585"></a>
<span id="l586">        <span class="sd">&quot;&quot;&quot;Dictionary style has_key() method.&quot;&quot;&quot;</span></span><a href="#l586"></a>
<span id="l587">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l587"></a>
<span id="l588">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">,</span> <span class="s">&quot;not indexable&quot;</span></span><a href="#l588"></a>
<span id="l589">        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="n">item</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="n">key</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="p">)</span></span><a href="#l589"></a>
<span id="l590"></span><a href="#l590"></a>
<span id="l591">    <span class="k">def</span> <span class="nf">__contains__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l591"></a>
<span id="l592">        <span class="sd">&quot;&quot;&quot;Dictionary style __contains__ method.&quot;&quot;&quot;</span></span><a href="#l592"></a>
<span id="l593">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l593"></a>
<span id="l594">            <span class="k">raise</span> <span class="ne">TypeError</span><span class="p">,</span> <span class="s">&quot;not indexable&quot;</span></span><a href="#l594"></a>
<span id="l595">        <span class="k">return</span> <span class="nb">any</span><span class="p">(</span><span class="n">item</span><span class="o">.</span><span class="n">name</span> <span class="o">==</span> <span class="n">key</span> <span class="k">for</span> <span class="n">item</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="p">)</span></span><a href="#l595"></a>
<span id="l596"></span><a href="#l596"></a>
<span id="l597">    <span class="k">def</span> <span class="nf">__len__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l597"></a>
<span id="l598">        <span class="sd">&quot;&quot;&quot;Dictionary style len(x) support.&quot;&quot;&quot;</span></span><a href="#l598"></a>
<span id="l599">        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">keys</span><span class="p">())</span></span><a href="#l599"></a>
<span id="l600"></span><a href="#l600"></a>
<span id="l601">    <span class="k">def</span> <span class="nf">__nonzero__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l601"></a>
<span id="l602">        <span class="k">return</span> <span class="nb">bool</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="p">)</span></span><a href="#l602"></a>
<span id="l603"></span><a href="#l603"></a>
<span id="l604">    <span class="k">def</span> <span class="nf">read_urlencoded</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l604"></a>
<span id="l605">        <span class="sd">&quot;&quot;&quot;Internal: read data in query string format.&quot;&quot;&quot;</span></span><a href="#l605"></a>
<span id="l606">        <span class="n">qs</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">length</span><span class="p">)</span></span><a href="#l606"></a>
<span id="l607">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">qs_on_post</span><span class="p">:</span></span><a href="#l607"></a>
<span id="l608">            <span class="n">qs</span> <span class="o">+=</span> <span class="s">&#39;&amp;&#39;</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">qs_on_post</span></span><a href="#l608"></a>
<span id="l609">        <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="o">=</span> <span class="nb">list</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l609"></a>
<span id="l610">        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">urlparse</span><span class="o">.</span><span class="n">parse_qsl</span><span class="p">(</span><span class="n">qs</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">keep_blank_values</span><span class="p">,</span></span><a href="#l610"></a>
<span id="l611">                                            <span class="bp">self</span><span class="o">.</span><span class="n">strict_parsing</span><span class="p">):</span></span><a href="#l611"></a>
<span id="l612">            <span class="nb">list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">MiniFieldStorage</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">))</span></span><a href="#l612"></a>
<span id="l613">        <span class="bp">self</span><span class="o">.</span><span class="n">skip_lines</span><span class="p">()</span></span><a href="#l613"></a>
<span id="l614"></span><a href="#l614"></a>
<span id="l615">    <span class="n">FieldStorageClass</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l615"></a>
<span id="l616"></span><a href="#l616"></a>
<span id="l617">    <span class="k">def</span> <span class="nf">read_multi</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">environ</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="p">):</span></span><a href="#l617"></a>
<span id="l618">        <span class="sd">&quot;&quot;&quot;Internal: read a part that is itself multipart.&quot;&quot;&quot;</span></span><a href="#l618"></a>
<span id="l619">        <span class="n">ib</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">innerboundary</span></span><a href="#l619"></a>
<span id="l620">        <span class="k">if</span> <span class="ow">not</span> <span class="n">valid_boundary</span><span class="p">(</span><span class="n">ib</span><span class="p">):</span></span><a href="#l620"></a>
<span id="l621">            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">,</span> <span class="s">&#39;Invalid boundary in multipart form: </span><span class="si">%r</span><span class="s">&#39;</span> <span class="o">%</span> <span class="p">(</span><span class="n">ib</span><span class="p">,)</span></span><a href="#l621"></a>
<span id="l622">        <span class="bp">self</span><span class="o">.</span><span class="n">list</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l622"></a>
<span id="l623">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">qs_on_post</span><span class="p">:</span></span><a href="#l623"></a>
<span id="l624">            <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">urlparse</span><span class="o">.</span><span class="n">parse_qsl</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">qs_on_post</span><span class="p">,</span></span><a href="#l624"></a>
<span id="l625">                                <span class="bp">self</span><span class="o">.</span><span class="n">keep_blank_values</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">strict_parsing</span><span class="p">):</span></span><a href="#l625"></a>
<span id="l626">                <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">MiniFieldStorage</span><span class="p">(</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">))</span></span><a href="#l626"></a>
<span id="l627">            <span class="n">FieldStorageClass</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l627"></a>
<span id="l628"></span><a href="#l628"></a>
<span id="l629">        <span class="n">klass</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">FieldStorageClass</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">__class__</span></span><a href="#l629"></a>
<span id="l630">        <span class="n">part</span> <span class="o">=</span> <span class="n">klass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fp</span><span class="p">,</span> <span class="p">{},</span> <span class="n">ib</span><span class="p">,</span></span><a href="#l630"></a>
<span id="l631">                     <span class="n">environ</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="p">)</span></span><a href="#l631"></a>
<span id="l632">        <span class="c"># Throw first part away</span></span><a href="#l632"></a>
<span id="l633">        <span class="k">while</span> <span class="ow">not</span> <span class="n">part</span><span class="o">.</span><span class="n">done</span><span class="p">:</span></span><a href="#l633"></a>
<span id="l634">            <span class="n">headers</span> <span class="o">=</span> <span class="n">rfc822</span><span class="o">.</span><span class="n">Message</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fp</span><span class="p">)</span></span><a href="#l634"></a>
<span id="l635">            <span class="n">part</span> <span class="o">=</span> <span class="n">klass</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">fp</span><span class="p">,</span> <span class="n">headers</span><span class="p">,</span> <span class="n">ib</span><span class="p">,</span></span><a href="#l635"></a>
<span id="l636">                         <span class="n">environ</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="p">)</span></span><a href="#l636"></a>
<span id="l637">            <span class="bp">self</span><span class="o">.</span><span class="n">list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">part</span><span class="p">)</span></span><a href="#l637"></a>
<span id="l638">        <span class="bp">self</span><span class="o">.</span><span class="n">skip_lines</span><span class="p">()</span></span><a href="#l638"></a>
<span id="l639"></span><a href="#l639"></a>
<span id="l640">    <span class="k">def</span> <span class="nf">read_single</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l640"></a>
<span id="l641">        <span class="sd">&quot;&quot;&quot;Internal: read an atomic part.&quot;&quot;&quot;</span></span><a href="#l641"></a>
<span id="l642">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">length</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l642"></a>
<span id="l643">            <span class="bp">self</span><span class="o">.</span><span class="n">read_binary</span><span class="p">()</span></span><a href="#l643"></a>
<span id="l644">            <span class="bp">self</span><span class="o">.</span><span class="n">skip_lines</span><span class="p">()</span></span><a href="#l644"></a>
<span id="l645">        <span class="k">else</span><span class="p">:</span></span><a href="#l645"></a>
<span id="l646">            <span class="bp">self</span><span class="o">.</span><span class="n">read_lines</span><span class="p">()</span></span><a href="#l646"></a>
<span id="l647">        <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">seek</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span></span><a href="#l647"></a>
<span id="l648"></span><a href="#l648"></a>
<span id="l649">    <span class="n">bufsize</span> <span class="o">=</span> <span class="mi">8</span><span class="o">*</span><span class="mi">1024</span>            <span class="c"># I/O buffering size for copy to file</span></span><a href="#l649"></a>
<span id="l650"></span><a href="#l650"></a>
<span id="l651">    <span class="k">def</span> <span class="nf">read_binary</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l651"></a>
<span id="l652">        <span class="sd">&quot;&quot;&quot;Internal: read binary data.&quot;&quot;&quot;</span></span><a href="#l652"></a>
<span id="l653">        <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_file</span><span class="p">(</span><span class="s">&#39;b&#39;</span><span class="p">)</span></span><a href="#l653"></a>
<span id="l654">        <span class="n">todo</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">length</span></span><a href="#l654"></a>
<span id="l655">        <span class="k">if</span> <span class="n">todo</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l655"></a>
<span id="l656">            <span class="k">while</span> <span class="n">todo</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span></span><a href="#l656"></a>
<span id="l657">                <span class="n">data</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">read</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">todo</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">bufsize</span><span class="p">))</span></span><a href="#l657"></a>
<span id="l658">                <span class="k">if</span> <span class="ow">not</span> <span class="n">data</span><span class="p">:</span></span><a href="#l658"></a>
<span id="l659">                    <span class="bp">self</span><span class="o">.</span><span class="n">done</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l659"></a>
<span id="l660">                    <span class="k">break</span></span><a href="#l660"></a>
<span id="l661">                <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></span><a href="#l661"></a>
<span id="l662">                <span class="n">todo</span> <span class="o">=</span> <span class="n">todo</span> <span class="o">-</span> <span class="nb">len</span><span class="p">(</span><span class="n">data</span><span class="p">)</span></span><a href="#l662"></a>
<span id="l663"></span><a href="#l663"></a>
<span id="l664">    <span class="k">def</span> <span class="nf">read_lines</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l664"></a>
<span id="l665">        <span class="sd">&quot;&quot;&quot;Internal: read lines until EOF or outerboundary.&quot;&quot;&quot;</span></span><a href="#l665"></a>
<span id="l666">        <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">__file</span> <span class="o">=</span> <span class="n">StringIO</span><span class="p">()</span></span><a href="#l666"></a>
<span id="l667">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">outerboundary</span><span class="p">:</span></span><a href="#l667"></a>
<span id="l668">            <span class="bp">self</span><span class="o">.</span><span class="n">read_lines_to_outerboundary</span><span class="p">()</span></span><a href="#l668"></a>
<span id="l669">        <span class="k">else</span><span class="p">:</span></span><a href="#l669"></a>
<span id="l670">            <span class="bp">self</span><span class="o">.</span><span class="n">read_lines_to_eof</span><span class="p">()</span></span><a href="#l670"></a>
<span id="l671"></span><a href="#l671"></a>
<span id="l672">    <span class="k">def</span> <span class="nf">__write</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">line</span><span class="p">):</span></span><a href="#l672"></a>
<span id="l673">        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__file</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l673"></a>
<span id="l674">            <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">__file</span><span class="o">.</span><span class="n">tell</span><span class="p">()</span> <span class="o">+</span> <span class="nb">len</span><span class="p">(</span><span class="n">line</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1000</span><span class="p">:</span></span><a href="#l674"></a>
<span id="l675">                <span class="bp">self</span><span class="o">.</span><span class="n">file</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">make_file</span><span class="p">(</span><span class="s">&#39;&#39;</span><span class="p">)</span></span><a href="#l675"></a>
<span id="l676">                <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">__file</span><span class="o">.</span><span class="n">getvalue</span><span class="p">())</span></span><a href="#l676"></a>
<span id="l677">                <span class="bp">self</span><span class="o">.</span><span class="n">__file</span> <span class="o">=</span> <span class="bp">None</span></span><a href="#l677"></a>
<span id="l678">        <span class="bp">self</span><span class="o">.</span><span class="n">file</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></span><a href="#l678"></a>
<span id="l679"></span><a href="#l679"></a>
<span id="l680">    <span class="k">def</span> <span class="nf">read_lines_to_eof</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l680"></a>
<span id="l681">        <span class="sd">&quot;&quot;&quot;Internal: read lines until EOF.&quot;&quot;&quot;</span></span><a href="#l681"></a>
<span id="l682">        <span class="k">while</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l682"></a>
<span id="l683">            <span class="n">line</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">readline</span><span class="p">(</span><span class="mi">1</span><span class="o">&lt;&lt;</span><span class="mi">16</span><span class="p">)</span></span><a href="#l683"></a>
<span id="l684">            <span class="k">if</span> <span class="ow">not</span> <span class="n">line</span><span class="p">:</span></span><a href="#l684"></a>
<span id="l685">                <span class="bp">self</span><span class="o">.</span><span class="n">done</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l685"></a>
<span id="l686">                <span class="k">break</span></span><a href="#l686"></a>
<span id="l687">            <span class="bp">self</span><span class="o">.</span><span class="n">__write</span><span class="p">(</span><span class="n">line</span><span class="p">)</span></span><a href="#l687"></a>
<span id="l688"></span><a href="#l688"></a>
<span id="l689">    <span class="k">def</span> <span class="nf">read_lines_to_outerboundary</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l689"></a>
<span id="l690">        <span class="sd">&quot;&quot;&quot;Internal: read lines until outerboundary.&quot;&quot;&quot;</span></span><a href="#l690"></a>
<span id="l691">        <span class="nb">next</span> <span class="o">=</span> <span class="s">&quot;--&quot;</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">outerboundary</span></span><a href="#l691"></a>
<span id="l692">        <span class="n">last</span> <span class="o">=</span> <span class="nb">next</span> <span class="o">+</span> <span class="s">&quot;--&quot;</span></span><a href="#l692"></a>
<span id="l693">        <span class="n">delim</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l693"></a>
<span id="l694">        <span class="n">last_line_lfend</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l694"></a>
<span id="l695">        <span class="k">while</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l695"></a>
<span id="l696">            <span class="n">line</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">readline</span><span class="p">(</span><span class="mi">1</span><span class="o">&lt;&lt;</span><span class="mi">16</span><span class="p">)</span></span><a href="#l696"></a>
<span id="l697">            <span class="k">if</span> <span class="ow">not</span> <span class="n">line</span><span class="p">:</span></span><a href="#l697"></a>
<span id="l698">                <span class="bp">self</span><span class="o">.</span><span class="n">done</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l698"></a>
<span id="l699">                <span class="k">break</span></span><a href="#l699"></a>
<span id="l700">            <span class="k">if</span> <span class="n">delim</span> <span class="o">==</span> <span class="s">&quot;</span><span class="se">\r</span><span class="s">&quot;</span><span class="p">:</span></span><a href="#l700"></a>
<span id="l701">                <span class="n">line</span> <span class="o">=</span> <span class="n">delim</span> <span class="o">+</span> <span class="n">line</span></span><a href="#l701"></a>
<span id="l702">                <span class="n">delim</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l702"></a>
<span id="l703">            <span class="k">if</span> <span class="n">line</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;--&quot;</span> <span class="ow">and</span> <span class="n">last_line_lfend</span><span class="p">:</span></span><a href="#l703"></a>
<span id="l704">                <span class="n">strippedline</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l704"></a>
<span id="l705">                <span class="k">if</span> <span class="n">strippedline</span> <span class="o">==</span> <span class="nb">next</span><span class="p">:</span></span><a href="#l705"></a>
<span id="l706">                    <span class="k">break</span></span><a href="#l706"></a>
<span id="l707">                <span class="k">if</span> <span class="n">strippedline</span> <span class="o">==</span> <span class="n">last</span><span class="p">:</span></span><a href="#l707"></a>
<span id="l708">                    <span class="bp">self</span><span class="o">.</span><span class="n">done</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l708"></a>
<span id="l709">                    <span class="k">break</span></span><a href="#l709"></a>
<span id="l710">            <span class="n">odelim</span> <span class="o">=</span> <span class="n">delim</span></span><a href="#l710"></a>
<span id="l711">            <span class="k">if</span> <span class="n">line</span><span class="p">[</span><span class="o">-</span><span class="mi">2</span><span class="p">:]</span> <span class="o">==</span> <span class="s">&quot;</span><span class="se">\r\n</span><span class="s">&quot;</span><span class="p">:</span></span><a href="#l711"></a>
<span id="l712">                <span class="n">delim</span> <span class="o">=</span> <span class="s">&quot;</span><span class="se">\r\n</span><span class="s">&quot;</span></span><a href="#l712"></a>
<span id="l713">                <span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="p">[:</span><span class="o">-</span><span class="mi">2</span><span class="p">]</span></span><a href="#l713"></a>
<span id="l714">                <span class="n">last_line_lfend</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l714"></a>
<span id="l715">            <span class="k">elif</span> <span class="n">line</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">:</span></span><a href="#l715"></a>
<span id="l716">                <span class="n">delim</span> <span class="o">=</span> <span class="s">&quot;</span><span class="se">\n</span><span class="s">&quot;</span></span><a href="#l716"></a>
<span id="l717">                <span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l717"></a>
<span id="l718">                <span class="n">last_line_lfend</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l718"></a>
<span id="l719">            <span class="k">elif</span> <span class="n">line</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;</span><span class="se">\r</span><span class="s">&quot;</span><span class="p">:</span></span><a href="#l719"></a>
<span id="l720">                <span class="c"># We may interrupt \r\n sequences if they span the 2**16</span></span><a href="#l720"></a>
<span id="l721">                <span class="c"># byte boundary</span></span><a href="#l721"></a>
<span id="l722">                <span class="n">delim</span> <span class="o">=</span> <span class="s">&quot;</span><span class="se">\r</span><span class="s">&quot;</span></span><a href="#l722"></a>
<span id="l723">                <span class="n">line</span> <span class="o">=</span> <span class="n">line</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span></span><a href="#l723"></a>
<span id="l724">                <span class="n">last_line_lfend</span> <span class="o">=</span> <span class="bp">False</span></span><a href="#l724"></a>
<span id="l725">            <span class="k">else</span><span class="p">:</span></span><a href="#l725"></a>
<span id="l726">                <span class="n">delim</span> <span class="o">=</span> <span class="s">&quot;&quot;</span></span><a href="#l726"></a>
<span id="l727">                <span class="n">last_line_lfend</span> <span class="o">=</span> <span class="bp">False</span></span><a href="#l727"></a>
<span id="l728">            <span class="bp">self</span><span class="o">.</span><span class="n">__write</span><span class="p">(</span><span class="n">odelim</span> <span class="o">+</span> <span class="n">line</span><span class="p">)</span></span><a href="#l728"></a>
<span id="l729"></span><a href="#l729"></a>
<span id="l730">    <span class="k">def</span> <span class="nf">skip_lines</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l730"></a>
<span id="l731">        <span class="sd">&quot;&quot;&quot;Internal: skip lines until outer boundary if defined.&quot;&quot;&quot;</span></span><a href="#l731"></a>
<span id="l732">        <span class="k">if</span> <span class="ow">not</span> <span class="bp">self</span><span class="o">.</span><span class="n">outerboundary</span> <span class="ow">or</span> <span class="bp">self</span><span class="o">.</span><span class="n">done</span><span class="p">:</span></span><a href="#l732"></a>
<span id="l733">            <span class="k">return</span></span><a href="#l733"></a>
<span id="l734">        <span class="nb">next</span> <span class="o">=</span> <span class="s">&quot;--&quot;</span> <span class="o">+</span> <span class="bp">self</span><span class="o">.</span><span class="n">outerboundary</span></span><a href="#l734"></a>
<span id="l735">        <span class="n">last</span> <span class="o">=</span> <span class="nb">next</span> <span class="o">+</span> <span class="s">&quot;--&quot;</span></span><a href="#l735"></a>
<span id="l736">        <span class="n">last_line_lfend</span> <span class="o">=</span> <span class="bp">True</span></span><a href="#l736"></a>
<span id="l737">        <span class="k">while</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l737"></a>
<span id="l738">            <span class="n">line</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">fp</span><span class="o">.</span><span class="n">readline</span><span class="p">(</span><span class="mi">1</span><span class="o">&lt;&lt;</span><span class="mi">16</span><span class="p">)</span></span><a href="#l738"></a>
<span id="l739">            <span class="k">if</span> <span class="ow">not</span> <span class="n">line</span><span class="p">:</span></span><a href="#l739"></a>
<span id="l740">                <span class="bp">self</span><span class="o">.</span><span class="n">done</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span></span><a href="#l740"></a>
<span id="l741">                <span class="k">break</span></span><a href="#l741"></a>
<span id="l742">            <span class="k">if</span> <span class="n">line</span><span class="p">[:</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="s">&quot;--&quot;</span> <span class="ow">and</span> <span class="n">last_line_lfend</span><span class="p">:</span></span><a href="#l742"></a>
<span id="l743">                <span class="n">strippedline</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l743"></a>
<span id="l744">                <span class="k">if</span> <span class="n">strippedline</span> <span class="o">==</span> <span class="nb">next</span><span class="p">:</span></span><a href="#l744"></a>
<span id="l745">                    <span class="k">break</span></span><a href="#l745"></a>
<span id="l746">                <span class="k">if</span> <span class="n">strippedline</span> <span class="o">==</span> <span class="n">last</span><span class="p">:</span></span><a href="#l746"></a>
<span id="l747">                    <span class="bp">self</span><span class="o">.</span><span class="n">done</span> <span class="o">=</span> <span class="mi">1</span></span><a href="#l747"></a>
<span id="l748">                    <span class="k">break</span></span><a href="#l748"></a>
<span id="l749">            <span class="n">last_line_lfend</span> <span class="o">=</span> <span class="n">line</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">&#39;</span><span class="se">\n</span><span class="s">&#39;</span><span class="p">)</span></span><a href="#l749"></a>
<span id="l750"></span><a href="#l750"></a>
<span id="l751">    <span class="k">def</span> <span class="nf">make_file</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">binary</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l751"></a>
<span id="l752">        <span class="sd">&quot;&quot;&quot;Overridable: return a readable &amp; writable file.</span></span><a href="#l752"></a>
<span id="l753"></span><a href="#l753"></a>
<span id="l754"><span class="sd">        The file will be used as follows:</span></span><a href="#l754"></a>
<span id="l755"><span class="sd">        - data is written to it</span></span><a href="#l755"></a>
<span id="l756"><span class="sd">        - seek(0)</span></span><a href="#l756"></a>
<span id="l757"><span class="sd">        - data is read from it</span></span><a href="#l757"></a>
<span id="l758"></span><a href="#l758"></a>
<span id="l759"><span class="sd">        The &#39;binary&#39; argument is unused -- the file is always opened</span></span><a href="#l759"></a>
<span id="l760"><span class="sd">        in binary mode.</span></span><a href="#l760"></a>
<span id="l761"></span><a href="#l761"></a>
<span id="l762"><span class="sd">        This version opens a temporary file for reading and writing,</span></span><a href="#l762"></a>
<span id="l763"><span class="sd">        and immediately deletes (unlinks) it.  The trick (on Unix!) is</span></span><a href="#l763"></a>
<span id="l764"><span class="sd">        that the file can still be used, but it can&#39;t be opened by</span></span><a href="#l764"></a>
<span id="l765"><span class="sd">        another process, and it will automatically be deleted when it</span></span><a href="#l765"></a>
<span id="l766"><span class="sd">        is closed or when the current process terminates.</span></span><a href="#l766"></a>
<span id="l767"></span><a href="#l767"></a>
<span id="l768"><span class="sd">        If you want a more permanent file, you derive a class which</span></span><a href="#l768"></a>
<span id="l769"><span class="sd">        overrides this method.  If you want a visible temporary file</span></span><a href="#l769"></a>
<span id="l770"><span class="sd">        that is nevertheless automatically deleted when the script</span></span><a href="#l770"></a>
<span id="l771"><span class="sd">        terminates, try defining a __del__ method in a derived class</span></span><a href="#l771"></a>
<span id="l772"><span class="sd">        which unlinks the temporary files you have created.</span></span><a href="#l772"></a>
<span id="l773"></span><a href="#l773"></a>
<span id="l774"><span class="sd">        &quot;&quot;&quot;</span></span><a href="#l774"></a>
<span id="l775">        <span class="kn">import</span> <span class="nn">tempfile</span></span><a href="#l775"></a>
<span id="l776">        <span class="k">return</span> <span class="n">tempfile</span><span class="o">.</span><span class="n">TemporaryFile</span><span class="p">(</span><span class="s">&quot;w+b&quot;</span><span class="p">)</span></span><a href="#l776"></a>
<span id="l777"></span><a href="#l777"></a>
<span id="l778"></span><a href="#l778"></a>
<span id="l779"></span><a href="#l779"></a>
<span id="l780"><span class="c"># Backwards Compatibility Classes</span></span><a href="#l780"></a>
<span id="l781"><span class="c"># ===============================</span></span><a href="#l781"></a>
<span id="l782"></span><a href="#l782"></a>
<span id="l783"><span class="k">class</span> <span class="nc">FormContentDict</span><span class="p">(</span><span class="n">UserDict</span><span class="o">.</span><span class="n">UserDict</span><span class="p">):</span></span><a href="#l783"></a>
<span id="l784">    <span class="sd">&quot;&quot;&quot;Form content as dictionary with a list of values per field.</span></span><a href="#l784"></a>
<span id="l785"></span><a href="#l785"></a>
<span id="l786"><span class="sd">    form = FormContentDict()</span></span><a href="#l786"></a>
<span id="l787"></span><a href="#l787"></a>
<span id="l788"><span class="sd">    form[key] -&gt; [value, value, ...]</span></span><a href="#l788"></a>
<span id="l789"><span class="sd">    key in form -&gt; Boolean</span></span><a href="#l789"></a>
<span id="l790"><span class="sd">    form.keys() -&gt; [key, key, ...]</span></span><a href="#l790"></a>
<span id="l791"><span class="sd">    form.values() -&gt; [[val, val, ...], [val, val, ...], ...]</span></span><a href="#l791"></a>
<span id="l792"><span class="sd">    form.items() -&gt;  [(key, [val, val, ...]), (key, [val, val, ...]), ...]</span></span><a href="#l792"></a>
<span id="l793"><span class="sd">    form.dict == {key: [val, val, ...], ...}</span></span><a href="#l793"></a>
<span id="l794"></span><a href="#l794"></a>
<span id="l795"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l795"></a>
<span id="l796">    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">environ</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">,</span> <span class="n">keep_blank_values</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">strict_parsing</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span></span><a href="#l796"></a>
<span id="l797">        <span class="bp">self</span><span class="o">.</span><span class="n">dict</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">data</span> <span class="o">=</span> <span class="n">parse</span><span class="p">(</span><span class="n">environ</span><span class="o">=</span><span class="n">environ</span><span class="p">,</span></span><a href="#l797"></a>
<span id="l798">                                      <span class="n">keep_blank_values</span><span class="o">=</span><span class="n">keep_blank_values</span><span class="p">,</span></span><a href="#l798"></a>
<span id="l799">                                      <span class="n">strict_parsing</span><span class="o">=</span><span class="n">strict_parsing</span><span class="p">)</span></span><a href="#l799"></a>
<span id="l800">        <span class="bp">self</span><span class="o">.</span><span class="n">query_string</span> <span class="o">=</span> <span class="n">environ</span><span class="p">[</span><span class="s">&#39;QUERY_STRING&#39;</span><span class="p">]</span></span><a href="#l800"></a>
<span id="l801"></span><a href="#l801"></a>
<span id="l802"></span><a href="#l802"></a>
<span id="l803"><span class="k">class</span> <span class="nc">SvFormContentDict</span><span class="p">(</span><span class="n">FormContentDict</span><span class="p">):</span></span><a href="#l803"></a>
<span id="l804">    <span class="sd">&quot;&quot;&quot;Form content as dictionary expecting a single value per field.</span></span><a href="#l804"></a>
<span id="l805"></span><a href="#l805"></a>
<span id="l806"><span class="sd">    If you only expect a single value for each field, then form[key]</span></span><a href="#l806"></a>
<span id="l807"><span class="sd">    will return that single value.  It will raise an IndexError if</span></span><a href="#l807"></a>
<span id="l808"><span class="sd">    that expectation is not true.  If you expect a field to have</span></span><a href="#l808"></a>
<span id="l809"><span class="sd">    possible multiple values, than you can use form.getlist(key) to</span></span><a href="#l809"></a>
<span id="l810"><span class="sd">    get all of the values.  values() and items() are a compromise:</span></span><a href="#l810"></a>
<span id="l811"><span class="sd">    they return single strings where there is a single value, and</span></span><a href="#l811"></a>
<span id="l812"><span class="sd">    lists of strings otherwise.</span></span><a href="#l812"></a>
<span id="l813"></span><a href="#l813"></a>
<span id="l814"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l814"></a>
<span id="l815">    <span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l815"></a>
<span id="l816">        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">])</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l816"></a>
<span id="l817">            <span class="k">raise</span> <span class="ne">IndexError</span><span class="p">,</span> <span class="s">&#39;expecting a single value&#39;</span></span><a href="#l817"></a>
<span id="l818">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></span><a href="#l818"></a>
<span id="l819">    <span class="k">def</span> <span class="nf">getlist</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l819"></a>
<span id="l820">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">]</span></span><a href="#l820"></a>
<span id="l821">    <span class="k">def</span> <span class="nf">values</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l821"></a>
<span id="l822">        <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l822"></a>
<span id="l823">        <span class="k">for</span> <span class="n">value</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="o">.</span><span class="n">values</span><span class="p">():</span></span><a href="#l823"></a>
<span id="l824">            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">value</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l824"></a>
<span id="l825">                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">value</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span></span><a href="#l825"></a>
<span id="l826">            <span class="k">else</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">value</span><span class="p">)</span></span><a href="#l826"></a>
<span id="l827">        <span class="k">return</span> <span class="n">result</span></span><a href="#l827"></a>
<span id="l828">    <span class="k">def</span> <span class="nf">items</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l828"></a>
<span id="l829">        <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l829"></a>
<span id="l830">        <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="o">.</span><span class="n">items</span><span class="p">():</span></span><a href="#l830"></a>
<span id="l831">            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">value</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span></span><a href="#l831"></a>
<span id="l832">                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">[</span><span class="mi">0</span><span class="p">]))</span></span><a href="#l832"></a>
<span id="l833">            <span class="k">else</span><span class="p">:</span> <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">key</span><span class="p">,</span> <span class="n">value</span><span class="p">))</span></span><a href="#l833"></a>
<span id="l834">        <span class="k">return</span> <span class="n">result</span></span><a href="#l834"></a>
<span id="l835"></span><a href="#l835"></a>
<span id="l836"></span><a href="#l836"></a>
<span id="l837"><span class="k">class</span> <span class="nc">InterpFormContentDict</span><span class="p">(</span><span class="n">SvFormContentDict</span><span class="p">):</span></span><a href="#l837"></a>
<span id="l838">    <span class="sd">&quot;&quot;&quot;This class is present for backwards compatibility only.&quot;&quot;&quot;</span></span><a href="#l838"></a>
<span id="l839">    <span class="k">def</span> <span class="nf">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l839"></a>
<span id="l840">        <span class="n">v</span> <span class="o">=</span> <span class="n">SvFormContentDict</span><span class="o">.</span><span class="n">__getitem__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">)</span></span><a href="#l840"></a>
<span id="l841">        <span class="k">if</span> <span class="n">v</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">in</span> <span class="s">&#39;0123456789+-.&#39;</span><span class="p">:</span></span><a href="#l841"></a>
<span id="l842">            <span class="k">try</span><span class="p">:</span> <span class="k">return</span> <span class="nb">int</span><span class="p">(</span><span class="n">v</span><span class="p">)</span></span><a href="#l842"></a>
<span id="l843">            <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span></span><a href="#l843"></a>
<span id="l844">                <span class="k">try</span><span class="p">:</span> <span class="k">return</span> <span class="nb">float</span><span class="p">(</span><span class="n">v</span><span class="p">)</span></span><a href="#l844"></a>
<span id="l845">                <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span> <span class="k">pass</span></span><a href="#l845"></a>
<span id="l846">        <span class="k">return</span> <span class="n">v</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l846"></a>
<span id="l847">    <span class="k">def</span> <span class="nf">values</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l847"></a>
<span id="l848">        <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l848"></a>
<span id="l849">        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span></span><a href="#l849"></a>
<span id="l850">            <span class="k">try</span><span class="p">:</span></span><a href="#l850"></a>
<span id="l851">                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">])</span></span><a href="#l851"></a>
<span id="l852">            <span class="k">except</span> <span class="ne">IndexError</span><span class="p">:</span></span><a href="#l852"></a>
<span id="l853">                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">])</span></span><a href="#l853"></a>
<span id="l854">        <span class="k">return</span> <span class="n">result</span></span><a href="#l854"></a>
<span id="l855">    <span class="k">def</span> <span class="nf">items</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l855"></a>
<span id="l856">        <span class="n">result</span> <span class="o">=</span> <span class="p">[]</span></span><a href="#l856"></a>
<span id="l857">        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">keys</span><span class="p">():</span></span><a href="#l857"></a>
<span id="l858">            <span class="k">try</span><span class="p">:</span></span><a href="#l858"></a>
<span id="l859">                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">key</span><span class="p">,</span> <span class="bp">self</span><span class="p">[</span><span class="n">key</span><span class="p">]))</span></span><a href="#l859"></a>
<span id="l860">            <span class="k">except</span> <span class="ne">IndexError</span><span class="p">:</span></span><a href="#l860"></a>
<span id="l861">                <span class="n">result</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">key</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">]))</span></span><a href="#l861"></a>
<span id="l862">        <span class="k">return</span> <span class="n">result</span></span><a href="#l862"></a>
<span id="l863"></span><a href="#l863"></a>
<span id="l864"></span><a href="#l864"></a>
<span id="l865"><span class="k">class</span> <span class="nc">FormContent</span><span class="p">(</span><span class="n">FormContentDict</span><span class="p">):</span></span><a href="#l865"></a>
<span id="l866">    <span class="sd">&quot;&quot;&quot;This class is present for backwards compatibility only.&quot;&quot;&quot;</span></span><a href="#l866"></a>
<span id="l867">    <span class="k">def</span> <span class="nf">values</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l867"></a>
<span id="l868">        <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span> <span class="p">:</span><span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">]</span></span><a href="#l868"></a>
<span id="l869">        <span class="k">else</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span></span><a href="#l869"></a>
<span id="l870">    <span class="k">def</span> <span class="nf">indexed_value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">,</span> <span class="n">location</span><span class="p">):</span></span><a href="#l870"></a>
<span id="l871">        <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">:</span></span><a href="#l871"></a>
<span id="l872">            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">])</span> <span class="o">&gt;</span> <span class="n">location</span><span class="p">:</span></span><a href="#l872"></a>
<span id="l873">                <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="n">location</span><span class="p">]</span></span><a href="#l873"></a>
<span id="l874">            <span class="k">else</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span></span><a href="#l874"></a>
<span id="l875">        <span class="k">else</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span></span><a href="#l875"></a>
<span id="l876">    <span class="k">def</span> <span class="nf">value</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l876"></a>
<span id="l877">        <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span></span><a href="#l877"></a>
<span id="l878">        <span class="k">else</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span></span><a href="#l878"></a>
<span id="l879">    <span class="k">def</span> <span class="nf">length</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l879"></a>
<span id="l880">        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">])</span></span><a href="#l880"></a>
<span id="l881">    <span class="k">def</span> <span class="nf">stripped</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span></span><a href="#l881"></a>
<span id="l882">        <span class="k">if</span> <span class="n">key</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">:</span> <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span><span class="p">[</span><span class="n">key</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span></span><a href="#l882"></a>
<span id="l883">        <span class="k">else</span><span class="p">:</span> <span class="k">return</span> <span class="bp">None</span></span><a href="#l883"></a>
<span id="l884">    <span class="k">def</span> <span class="nf">pars</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span></span><a href="#l884"></a>
<span id="l885">        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">dict</span></span><a href="#l885"></a>
<span id="l886"></span><a href="#l886"></a>
<span id="l887"></span><a href="#l887"></a>
<span id="l888"><span class="c"># Test/debug code</span></span><a href="#l888"></a>
<span id="l889"><span class="c"># ===============</span></span><a href="#l889"></a>
<span id="l890"></span><a href="#l890"></a>
<span id="l891"><span class="k">def</span> <span class="nf">test</span><span class="p">(</span><span class="n">environ</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">):</span></span><a href="#l891"></a>
<span id="l892">    <span class="sd">&quot;&quot;&quot;Robust test CGI script, usable as main program.</span></span><a href="#l892"></a>
<span id="l893"></span><a href="#l893"></a>
<span id="l894"><span class="sd">    Write minimal HTTP headers and dump all information provided to</span></span><a href="#l894"></a>
<span id="l895"><span class="sd">    the script in HTML form.</span></span><a href="#l895"></a>
<span id="l896"></span><a href="#l896"></a>
<span id="l897"><span class="sd">    &quot;&quot;&quot;</span></span><a href="#l897"></a>
<span id="l898">    <span class="k">print</span> <span class="s">&quot;Content-type: text/html&quot;</span></span><a href="#l898"></a>
<span id="l899">    <span class="k">print</span></span><a href="#l899"></a>
<span id="l900">    <span class="n">sys</span><span class="o">.</span><span class="n">stderr</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">stdout</span></span><a href="#l900"></a>
<span id="l901">    <span class="k">try</span><span class="p">:</span></span><a href="#l901"></a>
<span id="l902">        <span class="n">form</span> <span class="o">=</span> <span class="n">FieldStorage</span><span class="p">()</span>   <span class="c"># Replace with other classes to test those</span></span><a href="#l902"></a>
<span id="l903">        <span class="n">print_directory</span><span class="p">()</span></span><a href="#l903"></a>
<span id="l904">        <span class="n">print_arguments</span><span class="p">()</span></span><a href="#l904"></a>
<span id="l905">        <span class="n">print_form</span><span class="p">(</span><span class="n">form</span><span class="p">)</span></span><a href="#l905"></a>
<span id="l906">        <span class="n">print_environ</span><span class="p">(</span><span class="n">environ</span><span class="p">)</span></span><a href="#l906"></a>
<span id="l907">        <span class="n">print_environ_usage</span><span class="p">()</span></span><a href="#l907"></a>
<span id="l908">        <span class="k">def</span> <span class="nf">f</span><span class="p">():</span></span><a href="#l908"></a>
<span id="l909">            <span class="k">exec</span> <span class="s">&quot;testing print_exception() -- &lt;I&gt;italics?&lt;/I&gt;&quot;</span></span><a href="#l909"></a>
<span id="l910">        <span class="k">def</span> <span class="nf">g</span><span class="p">(</span><span class="n">f</span><span class="o">=</span><span class="n">f</span><span class="p">):</span></span><a href="#l910"></a>
<span id="l911">            <span class="n">f</span><span class="p">()</span></span><a href="#l911"></a>
<span id="l912">        <span class="k">print</span> <span class="s">&quot;&lt;H3&gt;What follows is a test, not an actual exception:&lt;/H3&gt;&quot;</span></span><a href="#l912"></a>
<span id="l913">        <span class="n">g</span><span class="p">()</span></span><a href="#l913"></a>
<span id="l914">    <span class="k">except</span><span class="p">:</span></span><a href="#l914"></a>
<span id="l915">        <span class="n">print_exception</span><span class="p">()</span></span><a href="#l915"></a>
<span id="l916"></span><a href="#l916"></a>
<span id="l917">    <span class="k">print</span> <span class="s">&quot;&lt;H1&gt;Second try with a small maxlen...&lt;/H1&gt;&quot;</span></span><a href="#l917"></a>
<span id="l918"></span><a href="#l918"></a>
<span id="l919">    <span class="k">global</span> <span class="n">maxlen</span></span><a href="#l919"></a>
<span id="l920">    <span class="n">maxlen</span> <span class="o">=</span> <span class="mi">50</span></span><a href="#l920"></a>
<span id="l921">    <span class="k">try</span><span class="p">:</span></span><a href="#l921"></a>
<span id="l922">        <span class="n">form</span> <span class="o">=</span> <span class="n">FieldStorage</span><span class="p">()</span>   <span class="c"># Replace with other classes to test those</span></span><a href="#l922"></a>
<span id="l923">        <span class="n">print_directory</span><span class="p">()</span></span><a href="#l923"></a>
<span id="l924">        <span class="n">print_arguments</span><span class="p">()</span></span><a href="#l924"></a>
<span id="l925">        <span class="n">print_form</span><span class="p">(</span><span class="n">form</span><span class="p">)</span></span><a href="#l925"></a>
<span id="l926">        <span class="n">print_environ</span><span class="p">(</span><span class="n">environ</span><span class="p">)</span></span><a href="#l926"></a>
<span id="l927">    <span class="k">except</span><span class="p">:</span></span><a href="#l927"></a>
<span id="l928">        <span class="n">print_exception</span><span class="p">()</span></span><a href="#l928"></a>
<span id="l929"></span><a href="#l929"></a>
<span id="l930"><span class="k">def</span> <span class="nf">print_exception</span><span class="p">(</span><span class="nb">type</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">value</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">tb</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">limit</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l930"></a>
<span id="l931">    <span class="k">if</span> <span class="nb">type</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span></span><a href="#l931"></a>
<span id="l932">        <span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">tb</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">exc_info</span><span class="p">()</span></span><a href="#l932"></a>
<span id="l933">    <span class="kn">import</span> <span class="nn">traceback</span></span><a href="#l933"></a>
<span id="l934">    <span class="k">print</span></span><a href="#l934"></a>
<span id="l935">    <span class="k">print</span> <span class="s">&quot;&lt;H3&gt;Traceback (most recent call last):&lt;/H3&gt;&quot;</span></span><a href="#l935"></a>
<span id="l936">    <span class="nb">list</span> <span class="o">=</span> <span class="n">traceback</span><span class="o">.</span><span class="n">format_tb</span><span class="p">(</span><span class="n">tb</span><span class="p">,</span> <span class="n">limit</span><span class="p">)</span> <span class="o">+</span> \</span><a href="#l936"></a>
<span id="l937">           <span class="n">traceback</span><span class="o">.</span><span class="n">format_exception_only</span><span class="p">(</span><span class="nb">type</span><span class="p">,</span> <span class="n">value</span><span class="p">)</span></span><a href="#l937"></a>
<span id="l938">    <span class="k">print</span> <span class="s">&quot;&lt;PRE&gt;</span><span class="si">%s</span><span class="s">&lt;B&gt;</span><span class="si">%s</span><span class="s">&lt;/B&gt;&lt;/PRE&gt;&quot;</span> <span class="o">%</span> <span class="p">(</span></span><a href="#l938"></a>
<span id="l939">        <span class="n">escape</span><span class="p">(</span><span class="s">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">list</span><span class="p">[:</span><span class="o">-</span><span class="mi">1</span><span class="p">])),</span></span><a href="#l939"></a>
<span id="l940">        <span class="n">escape</span><span class="p">(</span><span class="nb">list</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]),</span></span><a href="#l940"></a>
<span id="l941">        <span class="p">)</span></span><a href="#l941"></a>
<span id="l942">    <span class="k">del</span> <span class="n">tb</span></span><a href="#l942"></a>
<span id="l943"></span><a href="#l943"></a>
<span id="l944"><span class="k">def</span> <span class="nf">print_environ</span><span class="p">(</span><span class="n">environ</span><span class="o">=</span><span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">):</span></span><a href="#l944"></a>
<span id="l945">    <span class="sd">&quot;&quot;&quot;Dump the shell environment as HTML.&quot;&quot;&quot;</span></span><a href="#l945"></a>
<span id="l946">    <span class="n">keys</span> <span class="o">=</span> <span class="n">environ</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span></span><a href="#l946"></a>
<span id="l947">    <span class="n">keys</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></span><a href="#l947"></a>
<span id="l948">    <span class="k">print</span></span><a href="#l948"></a>
<span id="l949">    <span class="k">print</span> <span class="s">&quot;&lt;H3&gt;Shell Environment:&lt;/H3&gt;&quot;</span></span><a href="#l949"></a>
<span id="l950">    <span class="k">print</span> <span class="s">&quot;&lt;DL&gt;&quot;</span></span><a href="#l950"></a>
<span id="l951">    <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">keys</span><span class="p">:</span></span><a href="#l951"></a>
<span id="l952">        <span class="k">print</span> <span class="s">&quot;&lt;DT&gt;&quot;</span><span class="p">,</span> <span class="n">escape</span><span class="p">(</span><span class="n">key</span><span class="p">),</span> <span class="s">&quot;&lt;DD&gt;&quot;</span><span class="p">,</span> <span class="n">escape</span><span class="p">(</span><span class="n">environ</span><span class="p">[</span><span class="n">key</span><span class="p">])</span></span><a href="#l952"></a>
<span id="l953">    <span class="k">print</span> <span class="s">&quot;&lt;/DL&gt;&quot;</span></span><a href="#l953"></a>
<span id="l954">    <span class="k">print</span></span><a href="#l954"></a>
<span id="l955"></span><a href="#l955"></a>
<span id="l956"><span class="k">def</span> <span class="nf">print_form</span><span class="p">(</span><span class="n">form</span><span class="p">):</span></span><a href="#l956"></a>
<span id="l957">    <span class="sd">&quot;&quot;&quot;Dump the contents of a form as HTML.&quot;&quot;&quot;</span></span><a href="#l957"></a>
<span id="l958">    <span class="n">keys</span> <span class="o">=</span> <span class="n">form</span><span class="o">.</span><span class="n">keys</span><span class="p">()</span></span><a href="#l958"></a>
<span id="l959">    <span class="n">keys</span><span class="o">.</span><span class="n">sort</span><span class="p">()</span></span><a href="#l959"></a>
<span id="l960">    <span class="k">print</span></span><a href="#l960"></a>
<span id="l961">    <span class="k">print</span> <span class="s">&quot;&lt;H3&gt;Form Contents:&lt;/H3&gt;&quot;</span></span><a href="#l961"></a>
<span id="l962">    <span class="k">if</span> <span class="ow">not</span> <span class="n">keys</span><span class="p">:</span></span><a href="#l962"></a>
<span id="l963">        <span class="k">print</span> <span class="s">&quot;&lt;P&gt;No form fields.&quot;</span></span><a href="#l963"></a>
<span id="l964">    <span class="k">print</span> <span class="s">&quot;&lt;DL&gt;&quot;</span></span><a href="#l964"></a>
<span id="l965">    <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">keys</span><span class="p">:</span></span><a href="#l965"></a>
<span id="l966">        <span class="k">print</span> <span class="s">&quot;&lt;DT&gt;&quot;</span> <span class="o">+</span> <span class="n">escape</span><span class="p">(</span><span class="n">key</span><span class="p">)</span> <span class="o">+</span> <span class="s">&quot;:&quot;</span><span class="p">,</span></span><a href="#l966"></a>
<span id="l967">        <span class="n">value</span> <span class="o">=</span> <span class="n">form</span><span class="p">[</span><span class="n">key</span><span class="p">]</span></span><a href="#l967"></a>
<span id="l968">        <span class="k">print</span> <span class="s">&quot;&lt;i&gt;&quot;</span> <span class="o">+</span> <span class="n">escape</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="nb">type</span><span class="p">(</span><span class="n">value</span><span class="p">)))</span> <span class="o">+</span> <span class="s">&quot;&lt;/i&gt;&quot;</span></span><a href="#l968"></a>
<span id="l969">        <span class="k">print</span> <span class="s">&quot;&lt;DD&gt;&quot;</span> <span class="o">+</span> <span class="n">escape</span><span class="p">(</span><span class="nb">repr</span><span class="p">(</span><span class="n">value</span><span class="p">))</span></span><a href="#l969"></a>
<span id="l970">    <span class="k">print</span> <span class="s">&quot;&lt;/DL&gt;&quot;</span></span><a href="#l970"></a>
<span id="l971">    <span class="k">print</span></span><a href="#l971"></a>
<span id="l972"></span><a href="#l972"></a>
<span id="l973"><span class="k">def</span> <span class="nf">print_directory</span><span class="p">():</span></span><a href="#l973"></a>
<span id="l974">    <span class="sd">&quot;&quot;&quot;Dump the current directory as HTML.&quot;&quot;&quot;</span></span><a href="#l974"></a>
<span id="l975">    <span class="k">print</span></span><a href="#l975"></a>
<span id="l976">    <span class="k">print</span> <span class="s">&quot;&lt;H3&gt;Current Working Directory:&lt;/H3&gt;&quot;</span></span><a href="#l976"></a>
<span id="l977">    <span class="k">try</span><span class="p">:</span></span><a href="#l977"></a>
<span id="l978">        <span class="n">pwd</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">getcwd</span><span class="p">()</span></span><a href="#l978"></a>
<span id="l979">    <span class="k">except</span> <span class="n">os</span><span class="o">.</span><span class="n">error</span><span class="p">,</span> <span class="n">msg</span><span class="p">:</span></span><a href="#l979"></a>
<span id="l980">        <span class="k">print</span> <span class="s">&quot;os.error:&quot;</span><span class="p">,</span> <span class="n">escape</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">msg</span><span class="p">))</span></span><a href="#l980"></a>
<span id="l981">    <span class="k">else</span><span class="p">:</span></span><a href="#l981"></a>
<span id="l982">        <span class="k">print</span> <span class="n">escape</span><span class="p">(</span><span class="n">pwd</span><span class="p">)</span></span><a href="#l982"></a>
<span id="l983">    <span class="k">print</span></span><a href="#l983"></a>
<span id="l984"></span><a href="#l984"></a>
<span id="l985"><span class="k">def</span> <span class="nf">print_arguments</span><span class="p">():</span></span><a href="#l985"></a>
<span id="l986">    <span class="k">print</span></span><a href="#l986"></a>
<span id="l987">    <span class="k">print</span> <span class="s">&quot;&lt;H3&gt;Command Line Arguments:&lt;/H3&gt;&quot;</span></span><a href="#l987"></a>
<span id="l988">    <span class="k">print</span></span><a href="#l988"></a>
<span id="l989">    <span class="k">print</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span></span><a href="#l989"></a>
<span id="l990">    <span class="k">print</span></span><a href="#l990"></a>
<span id="l991"></span><a href="#l991"></a>
<span id="l992"><span class="k">def</span> <span class="nf">print_environ_usage</span><span class="p">():</span></span><a href="#l992"></a>
<span id="l993">    <span class="sd">&quot;&quot;&quot;Dump a list of environment variables used by CGI as HTML.&quot;&quot;&quot;</span></span><a href="#l993"></a>
<span id="l994">    <span class="k">print</span> <span class="s">&quot;&quot;&quot;</span></span><a href="#l994"></a>
<span id="l995"><span class="s">&lt;H3&gt;These environment variables could have been set:&lt;/H3&gt;</span></span><a href="#l995"></a>
<span id="l996"><span class="s">&lt;UL&gt;</span></span><a href="#l996"></a>
<span id="l997"><span class="s">&lt;LI&gt;AUTH_TYPE</span></span><a href="#l997"></a>
<span id="l998"><span class="s">&lt;LI&gt;CONTENT_LENGTH</span></span><a href="#l998"></a>
<span id="l999"><span class="s">&lt;LI&gt;CONTENT_TYPE</span></span><a href="#l999"></a>
<span id="l1000"><span class="s">&lt;LI&gt;DATE_GMT</span></span><a href="#l1000"></a>
<span id="l1001"><span class="s">&lt;LI&gt;DATE_LOCAL</span></span><a href="#l1001"></a>
<span id="l1002"><span class="s">&lt;LI&gt;DOCUMENT_NAME</span></span><a href="#l1002"></a>
<span id="l1003"><span class="s">&lt;LI&gt;DOCUMENT_ROOT</span></span><a href="#l1003"></a>
<span id="l1004"><span class="s">&lt;LI&gt;DOCUMENT_URI</span></span><a href="#l1004"></a>
<span id="l1005"><span class="s">&lt;LI&gt;GATEWAY_INTERFACE</span></span><a href="#l1005"></a>
<span id="l1006"><span class="s">&lt;LI&gt;LAST_MODIFIED</span></span><a href="#l1006"></a>
<span id="l1007"><span class="s">&lt;LI&gt;PATH</span></span><a href="#l1007"></a>
<span id="l1008"><span class="s">&lt;LI&gt;PATH_INFO</span></span><a href="#l1008"></a>
<span id="l1009"><span class="s">&lt;LI&gt;PATH_TRANSLATED</span></span><a href="#l1009"></a>
<span id="l1010"><span class="s">&lt;LI&gt;QUERY_STRING</span></span><a href="#l1010"></a>
<span id="l1011"><span class="s">&lt;LI&gt;REMOTE_ADDR</span></span><a href="#l1011"></a>
<span id="l1012"><span class="s">&lt;LI&gt;REMOTE_HOST</span></span><a href="#l1012"></a>
<span id="l1013"><span class="s">&lt;LI&gt;REMOTE_IDENT</span></span><a href="#l1013"></a>
<span id="l1014"><span class="s">&lt;LI&gt;REMOTE_USER</span></span><a href="#l1014"></a>
<span id="l1015"><span class="s">&lt;LI&gt;REQUEST_METHOD</span></span><a href="#l1015"></a>
<span id="l1016"><span class="s">&lt;LI&gt;SCRIPT_NAME</span></span><a href="#l1016"></a>
<span id="l1017"><span class="s">&lt;LI&gt;SERVER_NAME</span></span><a href="#l1017"></a>
<span id="l1018"><span class="s">&lt;LI&gt;SERVER_PORT</span></span><a href="#l1018"></a>
<span id="l1019"><span class="s">&lt;LI&gt;SERVER_PROTOCOL</span></span><a href="#l1019"></a>
<span id="l1020"><span class="s">&lt;LI&gt;SERVER_ROOT</span></span><a href="#l1020"></a>
<span id="l1021"><span class="s">&lt;LI&gt;SERVER_SOFTWARE</span></span><a href="#l1021"></a>
<span id="l1022"><span class="s">&lt;/UL&gt;</span></span><a href="#l1022"></a>
<span id="l1023"><span class="s">In addition, HTTP headers sent by the server may be passed in the</span></span><a href="#l1023"></a>
<span id="l1024"><span class="s">environment as well.  Here are some common variable names:</span></span><a href="#l1024"></a>
<span id="l1025"><span class="s">&lt;UL&gt;</span></span><a href="#l1025"></a>
<span id="l1026"><span class="s">&lt;LI&gt;HTTP_ACCEPT</span></span><a href="#l1026"></a>
<span id="l1027"><span class="s">&lt;LI&gt;HTTP_CONNECTION</span></span><a href="#l1027"></a>
<span id="l1028"><span class="s">&lt;LI&gt;HTTP_HOST</span></span><a href="#l1028"></a>
<span id="l1029"><span class="s">&lt;LI&gt;HTTP_PRAGMA</span></span><a href="#l1029"></a>
<span id="l1030"><span class="s">&lt;LI&gt;HTTP_REFERER</span></span><a href="#l1030"></a>
<span id="l1031"><span class="s">&lt;LI&gt;HTTP_USER_AGENT</span></span><a href="#l1031"></a>
<span id="l1032"><span class="s">&lt;/UL&gt;</span></span><a href="#l1032"></a>
<span id="l1033"><span class="s">&quot;&quot;&quot;</span></span><a href="#l1033"></a>
<span id="l1034"></span><a href="#l1034"></a>
<span id="l1035"></span><a href="#l1035"></a>
<span id="l1036"><span class="c"># Utilities</span></span><a href="#l1036"></a>
<span id="l1037"><span class="c"># =========</span></span><a href="#l1037"></a>
<span id="l1038"></span><a href="#l1038"></a>
<span id="l1039"><span class="k">def</span> <span class="nf">escape</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">quote</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span></span><a href="#l1039"></a>
<span id="l1040">    <span class="sd">&#39;&#39;&#39;Replace special characters &quot;&amp;&quot;, &quot;&lt;&quot; and &quot;&gt;&quot; to HTML-safe sequences.</span></span><a href="#l1040"></a>
<span id="l1041"><span class="sd">    If the optional flag quote is true, the quotation mark character (&quot;)</span></span><a href="#l1041"></a>
<span id="l1042"><span class="sd">    is also translated.&#39;&#39;&#39;</span></span><a href="#l1042"></a>
<span id="l1043">    <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&amp;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;amp;&quot;</span><span class="p">)</span> <span class="c"># Must be done first!</span></span><a href="#l1043"></a>
<span id="l1044">    <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&lt;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;lt;&quot;</span><span class="p">)</span></span><a href="#l1044"></a>
<span id="l1045">    <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&quot;&gt;&quot;</span><span class="p">,</span> <span class="s">&quot;&amp;gt;&quot;</span><span class="p">)</span></span><a href="#l1045"></a>
<span id="l1046">    <span class="k">if</span> <span class="n">quote</span><span class="p">:</span></span><a href="#l1046"></a>
<span id="l1047">        <span class="n">s</span> <span class="o">=</span> <span class="n">s</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">&#39;&quot;&#39;</span><span class="p">,</span> <span class="s">&quot;&amp;quot;&quot;</span><span class="p">)</span></span><a href="#l1047"></a>
<span id="l1048">    <span class="k">return</span> <span class="n">s</span></span><a href="#l1048"></a>
<span id="l1049"></span><a href="#l1049"></a>
<span id="l1050"><span class="k">def</span> <span class="nf">valid_boundary</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">_vb_pattern</span><span class="o">=</span><span class="s">&quot;^[ -~]{0,200}[!-~]$&quot;</span><span class="p">):</span></span><a href="#l1050"></a>
<span id="l1051">    <span class="kn">import</span> <span class="nn">re</span></span><a href="#l1051"></a>
<span id="l1052">    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">_vb_pattern</span><span class="p">,</span> <span class="n">s</span><span class="p">)</span></span><a href="#l1052"></a>
<span id="l1053"></span><a href="#l1053"></a>
<span id="l1054"><span class="c"># Invoke mainline</span></span><a href="#l1054"></a>
<span id="l1055"><span class="c"># ===============</span></span><a href="#l1055"></a>
<span id="l1056"></span><a href="#l1056"></a>
<span id="l1057"><span class="c"># Call test() when this file is run as a script (not imported as a module)</span></span><a href="#l1057"></a>
<span id="l1058"><span class="k">if</span> <span class="n">__name__</span> <span class="o">==</span> <span class="s">&#39;__main__&#39;</span><span class="p">:</span></span><a href="#l1058"></a>
<span id="l1059">    <span class="n">test</span><span class="p">()</span></span><a href="#l1059"></a></pre>
<div class="sourcelast"></div>
</div>
</div>
</div>

<script type="text/javascript">process_dates()</script>


</body>
</html>

