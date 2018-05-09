<!DOCTYPE html>

<body>

<h2><strong>Challenge 5</strong> - DNA Splicer</h2>

<p>HURRY! We need your help!<br>
We have a machine that we use to split, compare and match DNA samples, but it's been misbehaving and mixing the split
    samples with some others parts.<br>Given the parts can you reconstruct any of the original samples?</p>

<h4>Example:</h4>

<p>We have two samples 'aaccGgTTC'. One was split as 'aacc' 'GgTTC' and the other as 'aaccG' 'gTTC'. However these were
    mixed with parts 'aaaa' 'cccc' and 'gttc' from another experiment.
    <br>Given the input 'aacc GgTTC aaccG gTTC aaaa cccc gttc', the only possible original sample is 'aaccGgTTC',
    which can be formed twice with parts 1,2,3,4</p>

<h3>Notes</h3>

<p>You'll need to connect to 52.49.91.111:3241, and then type TEST or SUBMIT. But don't worry, you can reconnect and try
    as many times as you want.<br>
Daemon info messages start with '>'.<br>
You'll get a line with strings separated by ' '. These strings are the parts.<br>
You'll need to provide the 1 based indices ascending order of the parts that form the two chains when concatenated.<br>
You have to be fast! There's a timeout in each case.<br>
You're allowed at most 3 errors. The 4th error will disconnect you.<br>
The string given is 300 chars long maximum.<br>
There are at most 18 parts.<br>
It's guaranteed that there is at least one valid solution in each case.<br>
Chars a and A are different, same applies for c, C, t, T, g and G</p>

<h3>Sample Input as provided by the daemon</h3>

<p>
<pre>
aacc GgTTC aaccG gTTC aaaa cccc gttc
TATaCaACcCG aAgGacctcTtGgt TAttaCAtaTtA CgG TAttaCAtaTtAC CTATaCaACcCGcGg CCcCTaGcATaC cTgTGGAGAg cGgCgG
</pre>
</p>

<h3>Sample Output as required by the daemon</h3>
<p>
<pre>
1,2,3,4
1,3,4,5,6,9
</pre>
</p>
