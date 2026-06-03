---
search:
  boost: 10.0
---

# Class: ProvidedAsHybridCloudService 


_Technology provided as a cloud service that is both private and public_

_in parts_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsHybridCloudService](https://w3id.org/lmodel/dpv/tech/ProvidedAsHybridCloudService)





```mermaid
 classDiagram
    class ProvidedAsHybridCloudService
    click ProvidedAsHybridCloudService href "../ProvidedAsHybridCloudService/"
      ProvisionMethod <|-- ProvidedAsHybridCloudService
        click ProvisionMethod href "../ProvisionMethod/"
      ProvidedAsPublicCloudService <|-- ProvidedAsHybridCloudService
        click ProvidedAsPublicCloudService href "../ProvidedAsPublicCloudService/"
      ProvidedAsPrivateCloudService <|-- ProvidedAsHybridCloudService
        click ProvidedAsPrivateCloudService href "../ProvidedAsPrivateCloudService/"
      
      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * [ProvidedAsService](ProvidedAsService.md)
        * [ProvidedAsCloudService](ProvidedAsCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * [ProvidedAsPrivateCloudService](ProvidedAsPrivateCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
                * **ProvidedAsHybridCloudService** [ [ProvisionMethod](ProvisionMethod.md) [ProvidedAsPublicCloudService](ProvidedAsPublicCloudService.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsHybridCloudService](https://w3id.org/lmodel/dpv/tech/ProvidedAsHybridCloudService) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Hybrid Cloud ServiceProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsHybridCloudService |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsHybridCloudService |
| native | tech:ProvidedAsHybridCloudService |
| exact | dpv_tech:ProvidedAsHybridCloudService, dpv_tech_owl:ProvidedAsHybridCloudService |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsHybridCloudService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsHybridCloudService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service that is both private and public

  in parts'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Hybrid Cloud ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsHybridCloudService
- dpv_tech_owl:ProvidedAsHybridCloudService
is_a: ProvidedAsPrivateCloudService
mixins:
- ProvisionMethod
- ProvidedAsPublicCloudService
class_uri: tech:ProvidedAsHybridCloudService

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsHybridCloudService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsHybridCloudService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: 'Technology provided as a cloud service that is both private and public

  in parts'
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Hybrid Cloud ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsHybridCloudService
- dpv_tech_owl:ProvidedAsHybridCloudService
is_a: ProvidedAsPrivateCloudService
mixins:
- ProvisionMethod
- ProvidedAsPublicCloudService
class_uri: tech:ProvidedAsHybridCloudService

```
</details></div>