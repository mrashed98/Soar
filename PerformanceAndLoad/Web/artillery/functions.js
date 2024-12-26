const { faker } = require('@faker-js/faker');

function generateRegistrationData(requestParams, context, ee, next) {
  requestParams.form = {
    fullName: faker.person.fullName(),
    userName: faker.internet.userName(),
    email: faker.internet.email(),
    password: faker.internet.password(),
    phone: faker.phone.number()
  };
  return next();
}

function generateLoginData(requestParams, context, ee, next) {
  requestParams.form = {
    userName: faker.internet.userName(),
    email: faker.internet.email(),
    password: faker.internet.password()
  };
  return next();
}

module.exports = {
  generateRegistrationData,
  generateLoginData
};
