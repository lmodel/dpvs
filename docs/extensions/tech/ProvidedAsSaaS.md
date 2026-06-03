---
search:
  boost: 10.0
---

# Class: ProvidedAsSaaS 


_Technology provided as a cloud service consisting of managed software_

_resources_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsSaaS](https://w3id.org/lmodel/dpv/tech/ProvidedAsSaaS)





```mermaid
 classDiagram
    class ProvidedAsSaaS
    click ProvidedAsSaaS href "../ProvidedAsSaaS/"
      ProvisionMethod <|-- ProvidedAsSaaS
        click ProvisionMethod href "../ProvisionMethod/"
      ProvidedAsCloudService <|-- ProvidedAsSaaS
        click ProvidedAsCloudService href "../ProvidedAsCloudService/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * [ProvidedAsService](ProvidedAsService.md)
        * [ProvidedAsCloudService](ProvidedAsCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * **ProvidedAsSaaS** [ [ProvisionMethod](ProvisionMethod.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsSaaS](https://w3id.org/lmodel/dpv/tech/ProvidedAsSaaS) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Software as a Service (SaaS)Provision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsSaaS |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsSaaS |
| native | tech:ProvidedAsSaaS |
| exact | dpv_tech:ProvidedAsSaaS, dpv_tech_owl:ProvidedAsSaaS |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsSaaS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsSaaS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of managed software

  resources'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Software as a Service (SaaS)Provision
exact_mappings:
- dpv_tech:ProvidedAsSaaS
- dpv_tech_owl:ProvidedAsSaaS
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsSaaS

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsSaaS
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsSaaS
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service consisting of managed software

  resources'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Software as a Service (SaaS)Provision
exact_mappings:
- dpv_tech:ProvidedAsSaaS
- dpv_tech_owl:ProvidedAsSaaS
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsSaaS

```
</details></div>