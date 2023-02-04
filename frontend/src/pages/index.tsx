import Head from 'next/head'
import Image from 'next/image'
import { Inter, Roboto } from '@next/font/google'
import styles from '@/styles/Home.module.css'
import { useEffect, useState } from 'react'
import { getMorty, getRick } from '@/services/public.service'
import Dashboard from '@/Components/Dashboard'
import DashboardFix from '@/Components/Dashboard/DashboarFix'
import Layout from '@/containers/Layout/index'

const inter = Inter({ subsets: ['latin'] })

export default function Home() {
  return (
    <>
      <Head>
        <title>Create Next App</title>
        <meta name="description" content="Generated by create next app" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
        <Layout>
          <h1>Hola Mundo</h1>
        </Layout>
    </>
  )
}
