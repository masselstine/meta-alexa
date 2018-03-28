import logging

from random import randint
from flask import Flask, render_template
from flask_ask import Ask, statement, question, session

import subprocess
import thread
import pexpect


app = Flask(__name__)
ask = Ask(app, "/")

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def launch():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)

@ask.intent("container_list")
def container_list():
    list_msg = render_template('status')
    data = subprocess.check_output(["c3", "list"])
    linenum = 0
    for line in data.split('\n'):
        if linenum == 0 and "name" not in line:
            list_msg = render_template('list_error')
            break
        elif linenum > 1 and line.strip():
            # skip separator line
            parts = line.split()
            name = parts[0]
            state = parts[2]
            list_msg += " " + render_template('container')
            list_msg += " " + name
            list_msg += " " + render_template(state)
            list_msg += ","
        linenum = linenum + 1

    
    return statement(list_msg)

def do_install_container(name):
    pexpect.run("c3-cap --cap add %s.c3" % name)
    pexpect.run("c3 cmd c3-construct /var/lib/cube-cmd-server/functions.d/%s.c3" % name)

@ask.intent("install_container")
def install_container(container_name):
    inst_msg = render_template('install')
    inst_msg = inst_msg.replace("XXX", container_name)
    thread.start_new_thread(do_install_container, (container_name,))
    return statement(inst_msg)

def do_delete_container(name):
    pexpect.run("c3 delete %s" % name)

@ask.intent("delete_container")
def delete_container(container_name):
    del_msg = render_template('delete')
    del_msg = del_msg.replace("XXX", container_name)
    thread.start_new_thread(do_delete_container, (container_name,))
    return statement(del_msg)

def do_start_container(name):
    # Work around issues with 'c3 start' in the hub (something with running in script on dom0)
    pexpect.run("ssh dom0.cube.lan 'c3 start %s'" % name, events={'(?i)password':'incendia\n'})

@ask.intent("start_container")
def start_container(container_name):
    start_msg = render_template('start')
    start_msg = start_msg.replace("XXX", container_name)
    thread.start_new_thread(do_start_container, (container_name,))
    return statement(start_msg)

def do_stop_container(name):
    pexpect.run("c3 stop %s" % name)

@ask.intent("stop_container")
def stop_container(container_name):
    stop_msg = render_template('stop')
    stop_msg = stop_msg.replace("XXX", container_name)
    thread.start_new_thread(do_stop_container, (container_name,))
    return statement(stop_msg)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
