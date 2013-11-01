Kivy-testing
============

So, I was doing some tutorials from the kivy docs, and decided to share the results here.

This repo is for testing kivy. All kivy-related trash goes here too.

[![](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-1.png "WTFPL")](http://www.wtfpl.net/)

Run apps on android
-------------------
I made a simple script to automate the launching of kivy apps on android. It's tested and working in bash and zsh.

It's pretty simple to use:

1. You need to have the android platform-tools on your PC,  
your android needs to have USB Debugging enabled, and the kivy launcher app installed.  
Also, you need a kivy project directory with an `android.txt` file containing at least the `title=` value.  
The python file that gets run by the kivy launcher is `main.py`.

2. Add the script and the android platform-tools to your `$PATH`  
```export PATH=$PATH:/path/to/platform-tools:/path/to/dir/containing/kvrun```

3. `cd` to the kivy project directory and run:  
```kvrun [ip]```  
where `[ip]` is an optional value if you are using adb over wireless.
