import datetime
import os
import pathlib

root = pathlib.Path(__file__).parent.resolve()
DEMO_TOKEN = os.environ.get("DEMO_TOKEN", "")

if __name__ == "__main__":
    readme = root / "README.md"
    
    new_content = f'''
# Hi there 👋

Builder of things with code and the Cloud. Creator of pictures and videos. Explorer of minimalism. Learner.

📌  [Go and read my blog!](https://janik6n.net)

## 📚 Latest articles

- [Running Azure CLI in Docker container](https://janik6n.net/running-azure-cli-in-docker-container)
- [Makeshift Tree for macOS](https://janik6n.net/makeshift-tree-for-macos)
- [Azure App Service - "503 Service Unavailable"](https://janik6n.net/azure-app-service-503-service-unavailable)
- [Build a blog article in Markdown on the iPad with Shortcuts](https://janik6n.net/build-a-blog-article-in-markdown-on-the-ipad-with-shortcuts)

<!--
**janik6n/janik6n** is a ✨ _special_ ✨ repository because its `README.md` (this file) appears on your GitHub profile.

This is updated at {datetime.datetime.now()}.
{DEMO_TOKEN}.

Here are some ideas to get you started:

- 🔭 I’m currently working on ...
- 🌱 I’m currently learning ...
- 👯 I’m looking to collaborate on ...
- 🤔 I’m looking for help with ...
- 💬 Ask me about ...
- 📫 How to reach me: ...
- 😄 Pronouns: ...
- ⚡ Fun fact: ...
--> '''
        
    readme.open("w").write(new_content)
