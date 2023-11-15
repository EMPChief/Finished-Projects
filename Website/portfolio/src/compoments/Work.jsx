import React from 'react'
import Workitem from './Workitem'

const data = [
    {
        year: '2015',
        title: 'Fitjar Vidaregåande Skule',
        duration: '3 år',
        type: 'Utdanning',
        details: 'Fullførte kokkeskoleprogrammet.',
    },
    {
        year: '2018',
        title: 'Beredt Catering',
        duration: '2 år',
        type: 'Lærekandidat som institusjonskokk',
        details: 'Arbeidet med å skaffe kompetansebevis innen institusjonsmatlaging.',
    },
    {
        year: '2021',
        title: 'Subshore AS',
        duration: '1 år',
        type: 'Renholder og brannvakt',
        details: 'Utførte rengjøring på en plattform for sjøklargjøring. Var også brannvakt for sveisere av og til på båter.',
    },
    {
        year: '2021',
        title: 'Bremnes Seashore AS',
        duration: '2 måneder',
        type: 'Pakkeri',
        details: 'Utførte fiskefiletering og pakking av fisken i kasser.',
    },
    {
        year: '2022',
        title: 'Nova Sea As',
        duration: '2 år',
        type: 'Medarbeider',
        details: 'Har arbeidet med å filetere fisk, kjøre truck og snila for å transportere paller og klargjøre for forsendelse. I tillegg har jeg deltatt i fabrikkrengjøring, pakking av ryggbein, og forsegling av lokk på bokser før de blir sendt til kjøling for forsendelse.',
    },
]
const Work = () => {
  return (
    <div id='work' className='max-w-[1040px] m-auto md:pl-20 p-4 py-16'>
        <h1 className='text-4xl font-bold text-center text-green-500'>Work</h1>
        {data.map((item, idx) => (
            <Workitem key={idx} year={item.year} title={item.title} duration={item.duration} type={item.type} details={item.details} />
        ))}
    </div>
  )
}

export default Work