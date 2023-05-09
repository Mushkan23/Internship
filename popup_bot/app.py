from flask import Flask, render_template, request
import json
from brain import Brain

app = Flask(__name__)
