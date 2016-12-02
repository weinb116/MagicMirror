On a scale of 1 to 5, I give this code a rating of __5__ based on the following criteria:

1  The program has syntax errors and does not compile, or the project does not provide sufficient information to install necessary dependencies.
2  The program compiles successfully but generates runtime errors. or the project does not contain sufficient instructions to run the program.
3  The program compiles and runs but does not perform correctly and does not produce correct results
4  The program compiles and produces correct output but does not follow assignment/class guidelines or is insufficiently documented
5  The program produces correct output and is well written and well documented

Suggestions for improving the project:
I encountered a couple of syntax errors in the FacebookAPI.java file, namely with lines 5 and 6. Line 5 has an extra 'public static 
void' statement, and line 6 had a missing semicolon. Minor errors, ultimately. I cannot compile the program due to an error in line
1, which produces the following:

FacebookAPI.java:1: error: '.' expected
import restfb-1.34.1;
             ^
FacebookAPI.java:1: error: ';' expected
import restfb-1.34.1;
              ^
FacebookAPI.java:1: error: class, interface, or enum expected
import restfb-1.34.1;
                  ^
3 errors

For twitter.py, I could not compile the program beyond the first two string outputs. Attempting to compile the program results in the
following output:

Example 1
Establish Authentication Credentials
Traceback (most recent call last):
  File "twitter.py", line 9, in <module>
    import twitter
  File "/Users/seankeelan/MagicMirror/twitter.py", line 24, in <module>
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
AttributeError: 'module' object has no attribute 'oauth'

It is possible that this is the result of a user-end problem. As it stands, I have found no solution to the errors in 
FacebookAPI.java, nor to the AttributeError in twitter.py. I noticed that Perry did not encounter this problem, so I assume, again,
that it is an issue on my end.

WeatherAPI.java compiles and produces, as far as I am aware, correct output. Weather information is output in a neat and readable 
fashion. I would like to see a more detailed README.md file to more fully understand your goal with the project (I assume the goal is 
to create a user interface using a mirror, or something of the sort). You appear to have the tools for a weather application 
prepared, so I assume you have a direction for your project. I look forward to seeing the end product.
	- Sean K.