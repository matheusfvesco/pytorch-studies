# This script generates a BADGES.md inside the root 

# gets all ipynb relative paths as a list
BADGE_IPYNB_FILES=$(find . -type f -name "*.ipynb" | sed 's/^\.\///')

rm -f BADGES.md

echo "| Name | Colab|" >> BADGES.md
echo "| ---- | ---- |" >> BADGES.md

# creates markdown file
for file in $BADGE_IPYNB_FILES; do
  echo "| ${file} | <a href="https://colab.research.google.com/github/MYNAME/pytorch-studies/blob/main/${file}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>|" >> BADGES.md
done

# Use awk to replace content between <!-- BADGES --> and <!-- SEGDAB -->
awk -v new_content="$(cat BADGES.md)" '
  BEGIN { found = 0 }
  /<!-- BADGES -->/ { print; found = 1; print new_content; next }
  /<!-- SEGDAB -->/ { found = 0 }
  !found { print }
' README.md > README.tmp && mv README.tmp README.md

rm -f BADGES.md