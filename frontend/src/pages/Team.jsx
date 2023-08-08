// eslint-disable-next-line no-unused-vars
import React from 'react';
import Box from "../components/Imagebox";
const Team = () => {
  return (
    <div className="container mx-auto mt-8">
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <Box
          imageUrl="https://t3.ftcdn.net/jpg/01/97/11/64/360_F_197116416_hpfTtXSoJMvMqU99n6hGP4xX0ejYa4M7.jpg"
          altText="Image 1"
          text="Xingyu Bian - Product Manager"
        />
        <Box
          imageUrl="https://t3.ftcdn.net/jpg/01/97/11/64/360_F_197116416_hpfTtXSoJMvMqU99n6hGP4xX0ejYa4M7.jpg"
          altText="Image 2"
          text="Aaron Nguy - Backend"
        />
        <Box
          imageUrl="https://t3.ftcdn.net/jpg/01/97/11/64/360_F_197116416_hpfTtXSoJMvMqU99n6hGP4xX0ejYa4M7.jpg"
          altText="Image 3"
          text="Blake Almon - Backend"
        />
        <Box
          imageUrl="https://t3.ftcdn.net/jpg/01/97/11/64/360_F_197116416_hpfTtXSoJMvMqU99n6hGP4xX0ejYa4M7.jpg"
          altText="Image 4"
          text="Isaac Jung - Backend"
        />
        <Box
          imageUrl="https://t3.ftcdn.net/jpg/01/97/11/64/360_F_197116416_hpfTtXSoJMvMqU99n6hGP4xX0ejYa4M7.jpg"
          altText="Image 5"
          text="Jackson Pirooz - Frontend"
        />
        <Box
          imageUrl="https://t3.ftcdn.net/jpg/01/97/11/64/360_F_197116416_hpfTtXSoJMvMqU99n6hGP4xX0ejYa4M7.jpg"
          altText="Image 6"
          text="Lee Sophia - Frontend"
        />
      </div>
    </div>
  );
};

export default Team;
