export default function LoggedIn({ children }: { children: React.ReactNode }) {
  return (
    <div>
      <h1>Logged In</h1>
      <>
        {children}
      </>
    </div>
  );
}