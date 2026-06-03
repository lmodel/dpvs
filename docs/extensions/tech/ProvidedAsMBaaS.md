---
search:
  boost: 10.0
---

# Class: ProvidedAsMBaaS 


_Technology provided as a cloud service consisting of managed 'backend'_

_services for mobile users_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsMBaaS](https://w3id.org/lmodel/dpv/tech/ProvidedAsMBaaS)





```mermaid
 classDiagram
    class ProvidedAsMBaaS
    click ProvidedAsMBaaS href "../ProvidedAsMBaaS/"
      ProvisionMethod <|-- ProvidedAsMBaaS
        click ProvisionMethod href "../ProvisionMethod/"
      ProvidedAsCloudService <|-- ProvidedAsMBaaS
        click ProvidedAsCloudService href "../ProvidedAsCloudService/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * [ProvidedAsService](ProvidedAsService.md)
        * [ProvidedAsCloudService](ProvidedAsCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * **ProvidedAsMBaaS** [ [ProvisionMethod](ProvisionMethod.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsMBaaS](https://w3id.org/lmodel/dpv/tech/ProvidedAsMBaaS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Mobile backend as a ServiceProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsMBaaS |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsMBaaS |
| native | tech:ProvidedAsMBaaS |
| exact | dpv_tech:ProvidedAsMBaaS, dpv_tech_owl:ProvidedAsMBaaS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsMBaaS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsMBaaS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of managed ''backend''

  services for mobile users'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Mobile backend as a ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsMBaaS
- dpv_tech_owl:ProvidedAsMBaaS
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsMBaaS

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsMBaaS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsMBaaS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of managed ''backend''

  services for mobile users'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Mobile backend as a ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsMBaaS
- dpv_tech_owl:ProvidedAsMBaaS
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsMBaaS

```
</details></div>