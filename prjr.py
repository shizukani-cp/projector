import sys, argparse, shelve, subprocess, os
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("--project_name", "-p")
parser.add_argument("--program")
parser.add_argument("--projects_path")
args = parser.parse_args()

env = shelve.open("env")

if args.program:
    env["program"] = args.program

if args.projects_path:
    env["projects_path"] = args.projects_path

if (args.project_name is None) and (args.program or args.projects_path):  # When only the setting system is specified
    env.close()
    sys.exit()

program = env["program"]
projects_path = env["projects_path"]

if Path(args.project_name).is_absolute():
    project_path = Path(args.project_name)
else:
    project_path = Path(env["projects_path"]) / args.project_name

os.chdir(project_path)

subprocess.run(f'{env["program"]}', shell=True)

env["project_name"] = args.project_name

env.close()

