# Asymmetric encryption

Asymmetric Encryption uses two distinct, yet related keys. One key, the Public Key, is used for encryption and the other, the Private Key, is for decryption. As implied in the name, the Private Key is intended to be private so that only the authenticated recipient can decrypt the message(encrypted by the paired public key), The private key does not have to be shared with anyone whereas the public key is shared with the sender of the message, which is only used to encrypt the message. This eliminates security threats. 

## Key terminology

Explained above.
### Exercise

1. Generate a key pair.

2. Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. The recipient should be able to read the message, but it should remain a secret to everyone else.
You are not allowed to use any private messages or other communication channels besides Slack. Analyse the difference between this method and symmetric encryption.

### Sources

- [Asymmetric Encryption](https://www.youtube.com/watch?v=i-rtxrEz_E8)

- [Online RSA Key Generator](https://travistidwell.com/jsencrypt/demo/)

- [Public Key Cryptography - Computerphile](https://www.youtube.com/watch?v=GSIDS_lvRv4)

- [Pubic key encryption explained](https://www.cloudflare.com/learning/ssl/how-does-public-key-encryption-work/)

### Overcome challanges

I had to learn how asymmetric encryption works and understand how to generate keys using a key pair generator.
### Results

These are the steps i followed to send an asymmetric encrypted message to my teammate.  

- A key pair was generated using the Online RSA key generator link mentioned in sources.

- The public key was sent to the teammate in the Slack channel, and using that key a message was encrypted.

- Then the encrypted message was sent over again over the public channael (Slack). Anything encrypted with the public key, cannot be decrypted with the same key , so a corresponding private key(which was kept secret) is needed.

- Lastly, this corresponding private key was used to decrypt the message and read. Not everyone can read that message because they dont have the recipient's private key, which is great for confidentiality. 


![SEC-05-AsymmetricEncryption](../00_includes/SECURITIES/SEC-05/i1.png)

![SEC-05-AsymmetricEncryption](../00_includes/SECURITIES/SEC-05/i2.png)







