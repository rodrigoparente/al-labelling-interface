import LoginForm from "../features/LoginForm";
import LoggedOff from "../layouts/LoggedOff";

export default function LoginView() {

  return (
    <LoggedOff>
      <LoginForm />
    </LoggedOff>
  );
}