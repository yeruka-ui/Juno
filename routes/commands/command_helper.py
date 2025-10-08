from flask import jsonify, request
import json

def newJson(command, confidence, content):
    return jsonify({
        "isCommand": True,
        "command": f"{command}",
        "confidence": f"{confidence}",
        content: f"{content}"
    }), 200