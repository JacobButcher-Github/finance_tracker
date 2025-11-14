import { BrowserRouter, Routes, Route, NavLink } from "react-router";

import Dashboard from "./pages/dashboard";
import Income from "./pages/income";
import Expenditure from "./pages/expenditure";
import House from "./pages/house";
import Limits from "./pages/limits";
import Settings from "./pages/settings";
import Profile from "./pages/profile";
import "./stylesheets/main.scss";

const App: React.FC = () => {
  const navLinkClass = ({ isActive }: { isActive: boolean }) =>
    isActive ? "tab active" : "tab";
  const navLinkSettings = ({ isActive }: { isActive: boolean }) =>
    isActive ? "settings-button active" : "settings-button";
  const navLinkProfile = ({ isActive }: { isActive: boolean }) =>
    isActive ? "profile active" : "profile";

  return (
    <BrowserRouter>
      <nav className="navbar">
        <div className="left-tabs">
          <NavLink to="/" end className={navLinkClass}>
            Dashboard
          </NavLink>
          <NavLink to="/income" end className={navLinkClass}>
            Income
          </NavLink>
          <NavLink to="/expenditure" end className={navLinkClass}>
            Expenditure
          </NavLink>
          <NavLink to="/house" end className={navLinkClass}>
            House
          </NavLink>
          <NavLink to="/limits" end className={navLinkClass}>
            Limits
          </NavLink>
        </div>
        <div className="right-tabs">
          <label className="theme-switch">
            <input type="checkbox" />
            <span className="slider"></span>
          </label>
          <label className="mode-switch">
            <input type="checkbox" />
            <span className="slider"></span>
          </label>
          <NavLink to="/settings" end className={navLinkSettings}>
            Settings
          </NavLink>
          <NavLink to="/profile" end className={navLinkProfile}>
            Profile
          </NavLink>
        </div>
      </nav>
      <main>
        <Routes>
          <Route path="/" element={<Dashboard />}></Route>
          <Route path="/income" element={<Income />}></Route>
          <Route path="/expenditure" element={<Expenditure />}></Route>
          <Route path="/house" element={<House />}></Route>
          <Route path="/limits" element={<Limits />}></Route>
          <Route path="/settings" element={<Settings />}></Route>
          <Route path="/profile" element={<Profile />}></Route>
        </Routes>
      </main>
    </BrowserRouter>
  );
};

export default App;
