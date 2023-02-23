

const axios = require('axios');
const NodeRSA = require('node-rsa');

class Capital {
  constructor(state = {}) {
    this._state = state;

    this._api = axios.create({
      baseURL: BASE_URL,
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    });
  }

  async request(method, url, data = {}) {
    return await this._api({method, url, data,
      headers: {
        'CST': this._state.accessToken,
        'X-SECURITY-TOKEN': this._state.accountToken,
      },
    });
  }

  async requestAuth(method, url, data = {}) {
    return await this._api({method, url, data,
      headers: {
        'X-CAP-API-KEY': this._state.key,
      },
    });
  }

  async authenticate() {
    const { data, headers } = await this.requestAuth('post', '/session', {
      encryptedPassword: true,
      password: this._state.encryptedPassword,
      identifier: this._state.email,
    });

    this._state = {...this._state,
      accessToken: headers['cst'],
      accessTokenExpiresAt: Math.round(Date.now() / 1000) + 10 * 60, // in secs / 10 mins
      accountToken: headers['x-security-token'],
      account: data.currentAccountId,
    };

    return this._state;
  }

  async activate(credentials) {
    const [key, email, password] = credentials;

    this._state.key = key;

    const { data } = await this.requestAuth('get', '/session/encryptionKey');
    const { encryptionKey, timeStamp } = data;
    const encryptionKeyPem = `-----BEGIN PUBLIC KEY-----\n${encryptionKey}\n-----END PUBLIC KEY-----`;

    const rsaKey = new NodeRSA(encryptionKeyPem, {encryptionScheme: 'pkcs1'}); // critical
    const encryptedPassword = rsaKey.encrypt(password + '|' + timeStamp, 'base64');

    this._state = {...this._state, email, encryptedPassword};
    return this._state;
  }

  async getAccountList() {
    const { data } = await this.request('get', '/accounts');
    return data.accounts.filter(item => item.status === 'ENABLED');
  }
}

// Let's run it

(async () => {
  capital = new Capital();

  await capital.activate([
    'X-CAP-API-KEY_ADD_ME', // key
    'EMAIL_ADD_ME', // email
    'PASSWORD_ADD_ME', // password
  ]);

  // works well
  await capital.authenticate();
  await capital.getAccountList(); 

  // wait 10+ min
  await new Promise(resolve => setTimeout(resolve, 1000 * 60 * 10));

  // fails on re-authentication attempt :/
  await capital.authenticate();
  await capital.getAccountList();
})();


