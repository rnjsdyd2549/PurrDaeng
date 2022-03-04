import React, { useState, useRef, useEffect } from 'react';

const MyImageUpload = ({ files, id, checked, setChecked, setMainImg }: any) => {
  const imgRef: any = useRef([]);
  let main;

  const checkHandler = (num: any) => {
    main = imgRef.current[num].src;
    setMainImg(main);
    setChecked(num + 1);
  };

  useEffect(() => {
    if (files[id] !== undefined) {
      const imgEl1 = imgRef.current[id];
      imgEl1.src = files[id];
    } else {
      const imgEl1 = imgRef.current[id];
      imgEl1.src = `./img/tree.png`;
      setMainImg(files[0]);
    }
  }, [files]);
  return (
    <>
      <li className="relative" onClick={() => checkHandler(id)}>
        <img
          className="object-fill w-64 rounded-lg h-1/5 md:h-24"
          alt="나만의 식물"
          ref={elem => (imgRef.current[id] = elem)}
        />
        <div
          className={`absolute top-0 w-full h-full flex items-center justify-center  text-white rounded-lg m-0 ${
            checked === id + 1 ? `visible` : `invisible`
          }`}
          style={{ backgroundColor: 'rgba(0, 0, 0, 0.4)' }}
        >
          {id + 1}
        </div>
      </li>
    </>
  );
};

export default MyImageUpload;
