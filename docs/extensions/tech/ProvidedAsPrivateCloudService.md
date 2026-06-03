---
search:
  boost: 10.0
---

# Class: ProvidedAsPrivateCloudService 


_Technology provided as a cloud service that is private_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsPrivateCloudService](https://w3id.org/lmodel/dpv/tech/ProvidedAsPrivateCloudService)





```mermaid
 classDiagram
    class ProvidedAsPrivateCloudService
    click ProvidedAsPrivateCloudService href "../ProvidedAsPrivateCloudService/"
      ProvisionMethod <|-- ProvidedAsPrivateCloudService
        click ProvisionMethod href "../ProvisionMethod/"
      ProvidedAsCloudService <|-- ProvidedAsPrivateCloudService
        click ProvidedAsCloudService href "../ProvidedAsCloudService/"
      

      ProvidedAsPrivateCloudService <|-- ProvidedAsHybridCloudService
        click ProvidedAsHybridCloudService href "../ProvidedAsHybridCloudService/"
      

      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * [ProvidedAsService](ProvidedAsService.md)
        * [ProvidedAsCloudService](ProvidedAsCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * **ProvidedAsPrivateCloudService** [ [ProvisionMethod](ProvisionMethod.md)]
                * [ProvidedAsHybridCloudService](ProvidedAsHybridCloudService.md) [ [ProvisionMethod](ProvisionMethod.md) [ProvidedAsPublicCloudService](ProvidedAsPublicCloudService.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsPrivateCloudService](https://w3id.org/lmodel/dpv/tech/ProvidedAsPrivateCloudService) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Private Cloud ServiceProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsPrivateCloudService |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsPrivateCloudService |
| native | tech:ProvidedAsPrivateCloudService |
| exact | dpv_tech:ProvidedAsPrivateCloudService, dpv_tech_owl:ProvidedAsPrivateCloudService |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsPrivateCloudService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsPrivateCloudService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a cloud service that is private
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Private Cloud ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsPrivateCloudService
- dpv_tech_owl:ProvidedAsPrivateCloudService
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsPrivateCloudService

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsPrivateCloudService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsPrivateCloudService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a cloud service that is private
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Private Cloud ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsPrivateCloudService
- dpv_tech_owl:ProvidedAsPrivateCloudService
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsPrivateCloudService

```
</details></div>