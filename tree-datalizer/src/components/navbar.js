import { HStack, Link, Box, Image} from "@chakra-ui/react";

const Navbar = () => {
  return (
    <HStack spacing={4} alignItems="top">
        <Box boxSize='sm'>
            <Image src='treeDatalize.png' alt='TreeDatalize Logo' />
        </Box>
        <Link to= '/' colorScheme='pink'>Home</Link>
        <Link to= '/analytics'>Analytics</Link>
    </HStack>
  );
};

export default Navbar;
