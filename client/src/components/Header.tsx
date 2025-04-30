import "../styles/header.css";
import account from "../assets/account.svg";
import logo from "../assets/logo.svg";

const Header = () => {
  return (
    <>
      <header className="header">
        <div className="container container-flex">
          <img src={logo} className="logo" />
          <button
            className="account-btn"
            aria-label="Click to access the account section"
          >
            <img src={account} />
          </button>
        </div>
      </header>
    </>
  );
};

export default Header;
