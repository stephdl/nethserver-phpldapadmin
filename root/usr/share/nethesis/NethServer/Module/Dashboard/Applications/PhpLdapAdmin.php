<?php
namespace NethServer\Module\Dashboard\Applications;


/**
 * Phpldapadmin interface
 *
 * @author stephane de Labrusse
 */
class PhpLdapAdmin extends \Nethgui\Module\AbstractModule implements \NethServer\Module\Dashboard\Interfaces\ApplicationInterface
{

    public function getName()
    {
        return "PhpLdapAdmin";
    }

    public function getInfo()
    {
         $host = explode(':',$_SERVER['HTTP_HOST']);
         return array(
            'url' => "http://".$host[0]."/phpldapadmin/",
         );
    }
}


