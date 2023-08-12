from invoke import task
from pathlib import Path


def preflight_checklist():
    path = Path("tasks.py")
    if not path.exists():
        print("Run from root")
        exit()


# @task
# def copy_from_live(ctx, password, username="joannaru"):
#     """Download from live"""
#     preflight_checklist()

#     cmd = "rsync -arPv  joannaru@joannarubindranger.com:'~/public_html' ./"
#     print(cmd)
#     ctx.run(cmd, pty=True)


@task
def copy_to_live(ctx):
    """Download from live"""
    preflight_checklist()

    cmd = "rsync -arPv ./src/  joannaru@joannarubindranger.com:'~/public_html' "
    print(cmd)
    ctx.run(cmd, pty=True)
