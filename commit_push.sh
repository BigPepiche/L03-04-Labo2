git status
git add .
echo ""
echo ""
pwd
read -p "Enter a commit message: " commitMessage
git commit -m "$commitMessage"
git push

