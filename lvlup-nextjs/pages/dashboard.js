import Head from "next/head";
import { useState } from "react";
import useUser from "../hooks/apiCalls";
import LvlupSection from "../components/dashboard/LvlupSection";
import EntryList from "../components/dashboard/EntryList";
import styles from "../styles/Home.module.css";
import EntryModal from "../components/dashboard/EntryModal";

export default function Dashboard() {
  const { api_user, isError, isLoading, setUser } = useUser(1);
  const [showModal, setShowModal] = useState(false);

  const toggleModal = () => {
    setShowModal(!showModal);
  };

  if (isError) {
    return <div>Thewe was an ewwow lowding the page UwU</div>;
  }
  if (isLoading) {
    return <div>Loading page</div>;
  }
  if (api_user) {
    return (
      <div className={styles.container}>
        <Head>
          <title>Dashboard</title>
          <link rel="icon" href="/favicon.ico" />
        </Head>
        <LvlupSection api_user={api_user} />
        <EntryList entries={api_user.entries} toggleModal={toggleModal} />
        <EntryModal showModal={showModal} />
      </div>
    );
  }
  return "we failed";
}
