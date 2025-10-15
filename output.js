//Wed Oct 15 2025 08:49:09 GMT+0000 (Coordinated Universal Time)
//Base:https://github.com/echo094/decode-js
//Modify:https://github.com/smallfawn/decode_action
(function () {})();
(() => {
  const _0x47e6e0 = new TextEncoder(),
    _0x331ecf = new TextDecoder(),
    _0x1b4ca3 = "WssProxySecret-2025-ach";
  function _0xe69d4(_0xda909c) {
    const _0x362b20 = atob(_0xda909c),
      _0xadaace = _0x362b20.length,
      _0x2b0bc6 = new Uint8Array(_0xadaace);
    for (let _0x1cfeb2 = 0; _0x1cfeb2 < _0xadaace; _0x1cfeb2++) _0x2b0bc6[_0x1cfeb2] = _0x362b20.charCodeAt(_0x1cfeb2);
    return _0x2b0bc6;
  }
  async function _0x43208b() {
    {
      const _0x5d925a = await crypto.subtle.digest("SHA-256", _0x47e6e0.encode(_0x1b4ca3));
      return crypto.subtle.importKey("raw", _0x5d925a, {
        "name": "AES-GCM"
      }, false, ["decrypt"]);
    }
  }
  async function _0x43f519(_0xfeefb3) {
    {
      const _0x4112a4 = await _0x43208b(),
        _0x116a50 = _0xe69d4(_0xfeefb3.iv),
        _0x1c7b57 = _0xe69d4(_0xfeefb3.ciphertext),
        _0x3601d1 = _0xe69d4(_0xfeefb3.tag),
        _0x33cb2e = new Uint8Array(_0x1c7b57.length + _0x3601d1.length);
      _0x33cb2e.set(_0x1c7b57, 0);
      _0x33cb2e.set(_0x3601d1, _0x1c7b57.length);
      const _0x269509 = await crypto.subtle.decrypt({
        "name": "AES-GCM",
        "iv": _0x116a50,
        "tagLength": 128
      }, _0x4112a4, _0x33cb2e);
      return _0x331ecf.decode(_0x269509);
    }
  }
  async function _0x22b97d(_0x36d8fc) {
    {
      const _0x48dbc2 = await _0x43f519(_0x36d8fc);
      return JSON.parse(_0x48dbc2);
    }
  }
  window.ACHDecrypt = {
    "decryptPayload": _0x43f519,
    "decryptPayloadToObject": _0x22b97d
  };
})();