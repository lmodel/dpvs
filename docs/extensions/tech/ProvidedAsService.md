---
search:
  boost: 10.0
---

# Class: ProvidedAsService 


_Technology provided or used as service(s)_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsService](https://w3id.org/lmodel/dpv/tech/ProvidedAsService)





```mermaid
 classDiagram
    class ProvidedAsService
    click ProvidedAsService href "../ProvidedAsService/"
      ProvisionMethod <|-- ProvidedAsService
        click ProvisionMethod href "../ProvisionMethod/"
      

      ProvidedAsService <|-- ProvidedAsCloudService
        click ProvidedAsCloudService href "../ProvidedAsCloudService/"
      

      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * **ProvidedAsService**
        * [ProvidedAsCloudService](ProvidedAsCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsService](https://w3id.org/lmodel/dpv/tech/ProvidedAsService) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as ServiceProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsService |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsService |
| native | tech:ProvidedAsService |
| exact | dpv_tech:ProvidedAsService, dpv_tech_owl:ProvidedAsService |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided or used as service(s)
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsService
- dpv_tech_owl:ProvidedAsService
is_a: ProvisionMethod
class_uri: tech:ProvidedAsService

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided or used as service(s)
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsService
- dpv_tech_owl:ProvidedAsService
is_a: ProvisionMethod
class_uri: tech:ProvidedAsService

```
</details></div>