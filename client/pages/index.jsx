import Head from 'next/head'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import {faFacebook, faTwitter, faYoutube} from '@fortawesome/free-brands-svg-icons'
import MafiaMen from '../public/images/mafia-men.svg'
import Kanji from '../public/images/kanji.svg'

import {landing, content, logo, mafiaMen, socials, kanji} from '../styles/Landing.module.scss'

function HomePage() {
    return (
      <>
        <Head>
          <title>Vericane Mafia Magazine - Coming Soon</title>
          <link rel='icon' href='/images/favicon.ico'/>
        </Head>
        <div className={landing}>
          <div className={content}>
            <div className={logo}>
              <div className={mafiaMen}><MafiaMen/></div>
              <h1>VM.</h1>
            </div>
            <h2>Coming Soon</h2>
            <ul className={socials}>
              <li><a href="https://www.facebook.com/vericanemagazine/" target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faFacebook} /></a></li>
              <li><a href="https://twitter.com/vericanem?s=21" target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faTwitter} /></a></li>
              <li><a href="https://www.youtube.com/channel/UCCZprvo_ONvF7PLuVCPgv4g" target="_blank" rel="noopener noreferrer"><FontAwesomeIcon icon={faYoutube} /></a></li>
            </ul>
          </div>
          <div className={kanji}><Kanji/></div>
        </div>
      </>
    )
  }
  
  export default HomePage