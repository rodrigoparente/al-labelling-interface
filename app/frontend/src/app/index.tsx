import { BrowserRouter, Route, Routes } from 'react-router-dom'
import LoginView from './views/Login.view'
import RegistrationView from './views/Registration.view'
import WelcomeView from './views/Welcome.view'

export default function App () {
  return<BrowserRouter>
    <Routes>
      <Route path="/login" element={<LoginView />} />
      <Route path="/" element={<WelcomeView />} />
      <Route path="/registration" element={<RegistrationView />} />
      <Route path="/login" element={<LoginView />} />
    </Routes>
  </BrowserRouter>
}