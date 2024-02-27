from flask import Flask, render_template, request, redirect, Blueprint
import subprocess

func = Blueprint("func", __name__)
    
@func.route('/action/compile')
def compile():
    subprocess.run(['cd', '/app/c'])
    subprocess.run(['gcc', '-shared', '-O2', '-o', 'sample.so', 'sample.c'])
    return redirect('/')