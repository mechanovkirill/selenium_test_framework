
Short options guid:
1. "Browser"- implemented for Google Chrome and Firefox. 
      You can use it in the following way "Browser": "Chrome", or "Browser": "Firefox",

2. "Common_browsers_options" accepts a list of common browsers caps.
      Syntax: "Common_browsers_options": [{"page_load_strategy": "normal"}, {"browser_name": "Chrome"}],
      It is supporting capabilities page_load_strategy and browser_name.

3. "Chrome_options" and "Firefox_options" accepts browser specific functionality options.
      Syntax: "Chrome_options": ["--headless=new", "--start-maximized"], or  "Firefox_options": [],

4. "Explicit_wait_timeout" is common time for explicit waits in project. Accepts float.
      Syntax:   "Explicit_wait_timeout": 10,

5. "Explicit_wait_poll_frequency" is the frequency with which to check the condition in all waits in project. Accepts float. 
      Syntax: "Explicit_wait_poll_frequency": 1,

6. "Debug" determine the logging. If True, all log messages will be printed to the console. If False, messages will be 
wrote to the files: for INFO level and above and for WARNING level and above.  
      Syntax: "Debug": "False" or "Debug": "True" 