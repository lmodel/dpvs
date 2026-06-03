---
search:
  boost: 10.0
---

# Class: ProvidedAsCloudService 


_Technology provided as a cloud service_



<div data-search-exclude markdown="1">



URI: [tech:ProvidedAsCloudService](https://w3id.org/lmodel/dpv/tech/ProvidedAsCloudService)





```mermaid
 classDiagram
    class ProvidedAsCloudService
    click ProvidedAsCloudService href "../ProvidedAsCloudService/"
      ProvisionMethod <|-- ProvidedAsCloudService
        click ProvisionMethod href "../ProvisionMethod/"
      ProvidedAsService <|-- ProvidedAsCloudService
        click ProvidedAsService href "../ProvidedAsService/"
      

      ProvidedAsCloudService <|-- ProvidedAsCaaS
        click ProvidedAsCaaS href "../ProvidedAsCaaS/"
      ProvidedAsCloudService <|-- ProvidedAsIaaS
        click ProvidedAsIaaS href "../ProvidedAsIaaS/"
      ProvidedAsCloudService <|-- ProvidedAsMBaaS
        click ProvidedAsMBaaS href "../ProvidedAsMBaaS/"
      ProvidedAsCloudService <|-- ProvidedAsPaaS
        click ProvidedAsPaaS href "../ProvidedAsPaaS/"
      ProvidedAsCloudService <|-- ProvidedAsPrivateCloudService
        click ProvidedAsPrivateCloudService href "../ProvidedAsPrivateCloudService/"
      ProvidedAsCloudService <|-- ProvidedAsPublicCloudService
        click ProvidedAsPublicCloudService href "../ProvidedAsPublicCloudService/"
      ProvidedAsCloudService <|-- ProvidedAsSaaS
        click ProvidedAsSaaS href "../ProvidedAsSaaS/"
      ProvidedAsCloudService <|-- ProvidedAsServerlessComputing
        click ProvidedAsServerlessComputing href "../ProvidedAsServerlessComputing/"
      

      
```





## Inheritance
* [ProvisionMethod](ProvisionMethod.md)
    * [ProvidedAsService](ProvidedAsService.md)
        * **ProvidedAsCloudService** [ [ProvisionMethod](ProvisionMethod.md)]
            * [ProvidedAsCaaS](ProvidedAsCaaS.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * [ProvidedAsIaaS](ProvidedAsIaaS.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * [ProvidedAsMBaaS](ProvidedAsMBaaS.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * [ProvidedAsPaaS](ProvidedAsPaaS.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * [ProvidedAsPrivateCloudService](ProvidedAsPrivateCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * [ProvidedAsPublicCloudService](ProvidedAsPublicCloudService.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * [ProvidedAsSaaS](ProvidedAsSaaS.md) [ [ProvisionMethod](ProvisionMethod.md)]
            * [ProvidedAsServerlessComputing](ProvidedAsServerlessComputing.md) [ [ProvisionMethod](ProvisionMethod.md)]


## Class Properties

| Property | Value |
| --- | --- |
| Class URI | [tech:ProvidedAsCloudService](https://w3id.org/lmodel/dpv/tech/ProvidedAsCloudService) |


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |











## In Subsets


* [TechSubset](TechSubset.md)



## Aliases


* Provided as Cloud ServiceProvision




## Identifier and Mapping Information



### Annotations

| property | value |
| --- | --- |
| upstream_iri | https://w3id.org/dpv/tech/owl#ProvidedAsCloudService |
| dpv_extension_slug | tech |




### Schema Source


* from schema: https://w3id.org/lmodel/dpv/tech




## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | tech:ProvidedAsCloudService |
| native | tech:ProvidedAsCloudService |
| exact | dpv_tech:ProvidedAsCloudService, dpv_tech_owl:ProvidedAsCloudService |






## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: ProvidedAsCloudService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsCloudService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a cloud service
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Cloud ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsCloudService
- dpv_tech_owl:ProvidedAsCloudService
is_a: ProvidedAsService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsCloudService

```
</details>

### Induced

<details>
```yaml
name: ProvidedAsCloudService
annotations:
  upstream_iri:
    tag: upstream_iri
    value: https://w3id.org/dpv/tech/owl#ProvidedAsCloudService
  dpv_extension_slug:
    tag: dpv_extension_slug
    value: tech
description: Technology provided as a cloud service
in_subset:
- tech_subset
from_schema: https://w3id.org/lmodel/dpv/tech
aliases:
- Provided as Cloud ServiceProvision
exact_mappings:
- dpv_tech:ProvidedAsCloudService
- dpv_tech_owl:ProvidedAsCloudService
is_a: ProvidedAsService
mixins:
- ProvisionMethod
class_uri: tech:ProvidedAsCloudService

```
</details></div>