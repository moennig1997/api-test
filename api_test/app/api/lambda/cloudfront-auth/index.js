const { Authenticator } = require('cognito-at-edge');

const authenticator = new Authenticator({
  // Replace these parameter values with those of your own environment
  region: 'us-east-1', // user pool region
  userPoolId: 'us-east-1_eFKDdUrMd', // user pool ID
  userPoolAppId: '6am1ndih6o0vdfsagrppca1p8', // user pool app client ID
  userPoolDomain: 'cathead.auth.us-east-1.amazoncognito.com', // user pool domain
});

exports.handler = async (request) => authenticator.handle(request);