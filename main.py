#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re

#Global helper functions
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)

#Head
header = """
<head>
    <style>
        .error {color: red}
    </style>
</head>
"""

#Form
basic_form = """
<h1>Signup</h1>
<form method="post">
    <label = "username">
        Username:
    </label>
    <input type="text" name="username"/>
    <br>
    <label = "password">
        Password:
    </label>
    <input type="text" name="password"/>
    <br>
    <label = "verify_password">
        Verify Password:
    </label>
    <input type="text" name="verify"/>
    <br>
    <label = "email">
        E-Mail Address(Optional):
    </label>
    <input type="text" name="email"/>
    <br>
    <input type="submit" value="Submit"/>
</form>
"""

#Form iterations with Error Messages
invalidusr_form = """
<h1>Signup</h1>
<form method="post">
    <label = "username">
        Username:
    </label>
    <input type="text" name="username"/><span class="error">Invalid Username</span>
    <br>
    <label = "password">
        Password:
    </label>
    <input type="text" name="password"/>
    <br>
    <label = "verify_password">
        Verify Password:
    </label>
    <input type="text" name="verify"/>
    <br>
    <label = "email">
        E-Mail Address(Optional):
    </label>
    <input type="text" name="email"/>
    <br>
    <input type="submit" value="Submit"/>
</form>
"""

invalidpw_form = """
<h1>Signup</h1>
<form method="post">
    <label = "username">
        Username:
    </label>
    <input type="text" name="username"/>
    <br>
    <label = "password">
        Password:
    </label>
    <input type="text" name="password"/><span class="error">Invalid Password</span>
    <br>
    <label = "verify_password">
        Verify Password:
    </label>
    <input type="text" name="verify"/>
    <br>
    <label = "email">
        E-Mail Address(Optional):
    </label>
    <input type="text" name="email"/>
    <br>
    <input type="submit" value="Submit"/>
</form>
"""

passnomatch_form = """
<h1>Signup</h1>
<form method="post">
    <label = "username">
        Username:
    </label>
    <input type="text" name="username"/>
    <br>
    <label = "password">
        Password:
    </label>
    <input type="text" name="password"/>
    <br>
    <label = "verify_password">
        Verify Password:
    </label>
    <input type="text" name="verify"/><span class="error">Password does not match</span>
    <br>
    <label = "email">
        E-Mail Address(Optional):
    </label>
    <input type="text" name="email"/>
    <br>
    <input type="submit" value="Submit"/>
</form>
"""

invalidemail_form = """
<h1>Signup</h1>
<form method="post">
    <label = "username">
        Username:
    </label>
    <input type="text" name="username"/>
    <br>
    <label = "password">
        Password:
    </label>
    <input type="text" name="password"/>
    <br>
    <label = "verify_password">
        Verify Password:
    </label>
    <input type="text" name="verify"/>
    <br>
    <label = "email">
        E-Mail Address(Optional):
    </label>
    <input type="text" name="email"/><span class="error">Invalid Email</span>
    <br>
    <input type="submit" value="Submit"/>
</form>
"""

class MainHandler(webapp2.RequestHandler):

#MainHandler GET function
    def get(self):
        content = basic_form

        self.response.write(content)

#MainHandler POST function
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        content = "Thanks, bud!"

        if not valid_username(username):
            content = header + invalidusr_form

        if not valid_password(password):
            content = header + invalidpw_form

        elif password != verify:
            content = header + passnomatch_form

        if email and not valid_email(email):
            content = header + invalidemail_form

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
