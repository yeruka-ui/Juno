from flask import jsonify, request
import json

#returns new obj
def newJson(command, confidence, content):
    return jsonify({
        "isCommand": True,
        "command": command,
        "confidence": confidence,
        "content": content
    }), 200