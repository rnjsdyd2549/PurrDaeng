import React, { useRef, useEffect } from 'react';
import tw from 'tailwind-styled-components';

type MyImageProps = {
  files: string[];
  id: number;
  checked: number;
  setChecked: any;
};

const MyImageUpload = ({ files, id, checked, setChecked }: MyImageProps) => {
  const imgRef: any = useRef([]);

  const checkHandler = (num: any) => {
    setChecked(num + 1);
  };

  useEffect(() => {
    if (files[id] !== `./img/tree.png`) {
      const imgEl = imgRef.current[id];
      imgEl.src = files[id];
    } else {
      const imgEl = imgRef.current[id];
      imgEl.src = `./img/tree.png`;
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
        <Div
          className={` ${checked === id + 1 ? `visible` : `invisible`}`}
          style={{ backgroundColor: 'rgba(0, 0, 0, 0.4)' }}
        >
          {id + 1}
        </Div>
      </li>
    </>
  );
};

export default MyImageUpload;

const Div = tw.div`
  absolute
  top-0
  w-full
  h-full
  flex
  items-center
  justify-center
  text-white
  rounded-lg
  m-0
`;
