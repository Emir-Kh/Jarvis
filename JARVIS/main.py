from core.engine import JarvisEngine

jarvis = JarvisEngine()

from skills.app_launcher.scanner import scan_apps

apps = scan_apps()

print(len(apps))

jarvis.run()