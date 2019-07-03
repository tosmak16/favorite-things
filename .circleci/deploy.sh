sh ./.circleci/install-aws.sh
cd client
npm install
npm run build
aws s3 sync ./dist s3://favorite-things.tosmak.me/ --acl public-read --delete --exclude '.git/*'
