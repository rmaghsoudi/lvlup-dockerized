export default function LvlupSection(props) {
  const api_user = props.api_user;

  return (
    <div className="lvlup-section">
      Im the lvlup section, wus gud
      <progress
        id="lvlup-meter"
        value={api_user.xp}
        max={api_user.xp_to_lvlup}
      ></progress>
      <label htmlFor="lvlup-meter">
        Level {api_user.level}: {api_user.xp}xp / {api_user.xp_to_lvlup}xp
      </label>
    </div>
  );
}
