const config = window.FILM_CONFIG || {};
const player = document.querySelector("#drivePlayer");
const missingConfig = document.querySelector("#missingConfig");
const title = config.filmTitle || "C0030";
const fileId = config.driveFileId;

if (player && fileId && fileId !== "PUT_GOOGLE_DRIVE_FILE_ID_HERE") {
  player.title = title;
  player.src = `https://drive.google.com/file/d/${fileId}/preview`;
  missingConfig?.classList.add("is-hidden");
}
