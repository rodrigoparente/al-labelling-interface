import RegistrationForm from "../features/RegistrationForm";
import LoggedOff from "../layouts/LoggedOff";

export default function RegistrationView() {
  return (
    <LoggedOff>
      <RegistrationForm />
    </LoggedOff>
  );
}