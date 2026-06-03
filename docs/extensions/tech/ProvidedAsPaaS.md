---
search:
  boost: 10.0
---

# Class: ProvidedAsPaaS 


_Technology provided as a cloud service consisting of managed platform_

_resources_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsPaaS](https://w3id.org/lmodel/dpv/tech/ProvidedAsPaaS)





```mermaid
 classDiagram
    class ProvidedAsPaaS
    click ProvidedAsPaaS href "../ProvidedAsPaaS/"
      ProvisionMethod <|-- ProvidedAsPaaS
        click ProvisionMethod href "../ProvisionMethod/"
      ProvidedAsCloudService <|-- ProvidedAsPaaS
        click ProvidedAsCloudService href "../ProvidedAsCloudService/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * [ProvidedAsService](ProvidedAsService.md)
        * [ProvidedAsCloudService](ProvidedAsCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * **ProvidedAsPaaS** [ [ProvisionMethod](ProvisionMethod.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsPaaS](https://w3id.org/lmodel/dpv/tech/ProvidedAsPaaS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Platform as a Service (PaaS)Provision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsPaaS |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsPaaS |
| native | tech:ProvidedAsPaaS |
| exact | dpv_tech:ProvidedAsPaaS, dpv_tech_owl:ProvidedAsPaaS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsPaaS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsPaaS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of managed platform

  resources'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Platform as a Service (PaaS)Provision
exact_mappings:
- dpv_tech:ProvidedAsPaaS
- dpv_tech_owl:ProvidedAsPaaS
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsPaaS

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsPaaS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsPaaS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of managed platform

  resources'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Platform as a Service (PaaS)Provision
exact_mappings:
- dpv_tech:ProvidedAsPaaS
- dpv_tech_owl:ProvidedAsPaaS
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsPaaS

```
</details></div>