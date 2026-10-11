import re
from textwrap import indent
from typing import Type
from pathlib import Path

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Issue, Reporter
import json
import traceback

BASE_DIR = Path(__file__).resolve().parent

REPORTER_FILE_PATH = BASE_DIR / "resources" / "reporters.json"
ISSUES_FILE_PATH = BASE_DIR / "resources" / "issues.json"

# Create your views here.
@api_view(["POST"])
def create_reporter(request):
    try: 
        data = request.data

        reporter = Reporter(
                id=data["id"],
                name=data["name"],
                email=data["email"],
                team=data["team"],
            )

        reporter.validate()
        
        
        with open(REPORTER_FILE_PATH, "r") as file:
            content = file.read().strip()

        reporters = json.loads(content) if content else []

        for rep in reporters:
            if rep["id"] == reporter.id:
                return Response(
                                {"error": "Reporter ID already exists"},
                                status=400,
                            )
        reporters.append(reporter.to_dict())

        with open(REPORTER_FILE_PATH, "w") as file:
            json.dump(reporters, file, indent=4)

        return Response(reporter.to_dict(), status=201)

    except (KeyError, ValueError, TypeError) as e:
        traceback.print_exc()
        return Response({"error": str(e)}, status=400)

@api_view(["GET"])
def get_reporters(request, id=None):
    with open(REPORTER_FILE_PATH, "r") as file:
            content = file.read().strip()
            reporters = json.loads(content) if content else []

    if id is None:
        return Response(reporters)

    for rep in reporters:
        if rep["id"] == id:
            return Response(rep)

    return Response(
        {"error": "Reporter not found"},
        status=404
    )

@api_view(["POST"])
def create_issue(request):
    try:
        data = request.data

        issue = Issue(
            id = data["id"],
            title = data["title"],
            description = data["description"],
            status = data["status"],
            priority = data["priority"],
            reporter_id= data["reporter_id"]
        )

        issue.validate()

        with open(ISSUES_FILE_PATH, "r") as file:
            content = file.read().strip()

        issues = json.loads(content) if content else []

        for iss in issues:
            if iss["id"] == issue.id:
                return Response(
                                {"error": "Issue already exists"},
                                status=400,
                            )
        issues.append(issue.to_dict())

        with open(ISSUES_FILE_PATH, "w") as file:
            json.dump(issues, file, indent=4)

        return Response(issue.to_dict(), status=201)

    except (KeyError, ValueError, TypeError) as e:
        traceback.print_exc()
        return Response({"error": str(e)}, status=400)

@api_view(["GET"])
def get_issues(request):
    with open(ISSUES_FILE_PATH, "r") as file:
            content = file.read().strip()
            issues = json.loads(content) if content else []

    issue_id = request.query_params.get("id")

    if issue_id is None:
        return Response(issues)

    for issue in issues:
        if str(issue.get("id")) == issue_id.strip():
            return Response(issue)

    return Response(
        {"error": "Issue not found"},
        status=404
    )

@api_view(["GET"])
def get_open_issues(request):
    with open(ISSUES_FILE_PATH, "r") as file:
        content = file.read().strip()
        issues = json.loads(content) if content else []

    status = request.query_params.get("status")

    if status is None:
        return Response(issues)

    filtered_issues = [
        issue for issue in issues
        if issue.get("status", "").strip().lower() == status.strip().lower()
    ]

    if not filtered_issues:
        return Response(
            {"error": f"No issues found with status '{status}'"},
            status=404
        )

    return Response(filtered_issues)

    






