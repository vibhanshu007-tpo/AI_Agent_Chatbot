import streamlit as st
import streamlit_authenticator as stauth

# HASH PASSWORD
hashed_passwords = stauth.Hasher(['1234']).generate()

# CREDENTIALS
credentials = {
    "usernames": {
        "vibhanshu": {
            "name": "Vibhanshu",
            "password": hashed_passwords[0]
        }
    }
}

# AUTHENTICATOR
authenticator = stauth.Authenticate(
    credentials,
    "cookie_name",
    "signature_key",
    cookie_expiry_days=1
)

# LOGIN
name, authentication_status, username = authenticator.login(
    "Login",
    "main"
)

if authentication_status:
    st.success(f"Welcome {name}")

    authenticator.logout("Logout", "sidebar")

elif authentication_status == False:
    st.error("Incorrect username/password")

else:
    st.warning("Please login")