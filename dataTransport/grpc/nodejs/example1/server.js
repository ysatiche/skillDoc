const grpc = require('grpc')
const R = require('ramda')
const path = require('path')
const fs = require('fs')
var protoLoader = require('@grpc/proto-loader');

const PROTO_PATH = path.join(__dirname, './protos/test.proto')
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var hello_proto = grpc.loadPackageDefinition(packageDefinition).helloworld;

/**
 * Implements the SayHello RPC method.
 */
function sayHello1(call, callback) {
  console.log('call.request:', call.request)
  callback(null, {message: 'Hello ' + call.request.name});
}


/**
 * Starts an RPC server that receives requests for the Greeter service at the
 * sample server port
 */
function main() {
  var server = new grpc.Server();
  server.addService(hello_proto.Greeter.service, {sayHello: sayHello1});
  server.bind('0.0.0.0:50051', grpc.ServerCredentials.createInsecure());
  server.start();
}

main();