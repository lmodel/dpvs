---
search:
  boost: 10.0
---

# Class: ProvidedAsPublicCloudService 


_Technology provided as a cloud service that is public_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsPublicCloudService](https://w3id.org/lmodel/dpv/tech/ProvidedAsPublicCloudService)





```mermaid
 classDiagram
    class ProvidedAsPublicCloudService
    click ProvidedAsPublicCloudService href "../ProvidedAsPublicCloudService/"
      ProvisionMethod <|-- ProvidedAsPublicCloudService
        click ProvisionMethod href "../ProvisionMethod/"
      ProvidedAsCloudService <|-- ProvidedAsPublicCloudService
        click ProvidedAsCloudService href "../ProvidedAsCloudService/"
      

      ProvidedAsPublicCloudService <|-- ProvidedAsHybridCloudService
        click ProvidedAsHybridCloudService href "../ProvidedAsHybridCloudService/"
      

      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * [ProvidedAsService](ProvidedAsService.md)
        * [ProvidedAsCloudService](ProvidedAsCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * **ProvidedAsPublicCloudService** [ [ProvisionMethod](ProvisionMethod.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsPublicCloudService](https://w3id.org/lmodel/dpv/tech/ProvidedAsPublicCloudService) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Public Cloud ServiceProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsPublicCloudService |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsPublicCloudService |
| native | tech:ProvidedAsPublicCloudService |
| exact | dpv_tech:ProvidedAsPublicCloudService, dpv_tech_owl:ProvidedAsPublicCloudService |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsPublicCloudService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsPublicCloudService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a cloud service that is public
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Public Cloud ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsPublicCloudService
- dpv_tech_owl:ProvidedAsPublicCloudService
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsPublicCloudService

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsPublicCloudService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsPublicCloudService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a cloud service that is public
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Public Cloud ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsPublicCloudService
- dpv_tech_owl:ProvidedAsPublicCloudService
is_a: ProvidedAsCloudService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsPublicCloudService

```
</details></div>