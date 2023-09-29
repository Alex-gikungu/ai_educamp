from flask import Blueprint, request, jsonify
from backend.story import Story  # Corrected import
from backend.story import db  # Corrected import

story_bp = Blueprint("story", __name__)

@story_bp.route("/", methods=["POST"])
def generate_story():
    prompt = request.json["prompt"]

    story = Story(prompt=prompt)
    story.generate_story()

    db.session.add(story)
    db.session.commit()

    return jsonify({"story": story.story})

